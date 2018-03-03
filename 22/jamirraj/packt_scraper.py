import requests
import bs4
from datetime import datetime
from credentials import SENDER, RECIPIENTS, USERNAME, PWD

# URL of site we want to scrape
BASE_URL = "http://www.packtpub.com"
URL = BASE_URL + "/packt/offers/free-learning"
HEADERS = {'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}
AFFLIATION_LINK = 'https://www.packtpub.com/packt/offers/free-learning?utm_source=Pybonacci&utm_medium=referral&utm_campaign=FreeLearning2017CharityReferrals'


def main():
    raw_site_page = requests.get(URL, headers=HEADERS)
    raw_site_page.raise_for_status()

    # Create BeautifulSoup object
    soup = bs4.BeautifulSoup(raw_site_page.text, 'html.parser')

    # scrap information about the free book
    print('Scraping packthub..')
    book_meta_data = get_book_meta_data(soup)

    # get email html content
    email_content = construct_message(book_meta_data)
    subject = '{} left to claim {}'.format(book_meta_data['time_left'], book_meta_data['title'])

    # send an email notification with free book's details
    print('Sending email to {}'.format(RECIPIENTS))
    send_email_notification(RECIPIENTS, subject, email_content)
    print('Email sent.')


def get_book_meta_data(html_parser):
    book_meta_data = dict()

    # get book title
    book_title = html_parser.find('div', {"class": "dotd-title"})
    book_meta_data["title"] = book_title.find('h2').text.strip()

    # get book description
    book_description_div = html_parser.find('div', {'class': 'dotd-main-book-summary float-left'})
    book_description = book_description_div.findAll('div')
    book_meta_data["Description"] = book_description[2].text.strip()

    # get book's summary list
    book_summary_list = book_description_div.findAll('li')
    description_list = [li.text.strip() for li in book_summary_list]
    book_meta_data["Summary"] = description_list

    # get time left
    time_left_span = html_parser.find('span', {'class': 'packt-js-countdown'})
    book_meta_data["time_left"] = get_time_left(time_left_span.get('data-countdown-to'))

    # get book image
    book_image_div = html_parser.find('div', {"class": "dotd-main-book-image float-left"})
    book_meta_data['link'] = BASE_URL + book_image_div.find('a').get('href')
    book_meta_data['cover'] = 'https:' + book_image_div.find('img').get('src')

    return book_meta_data


def send_email_notification(recipients, subject, content):

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = ", ".join(recipients)
    message = MIMEText(content, 'html')
    msg.attach(message)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USERNAME, PWD)
    server.sendmail(SENDER, recipients, msg.as_string())


def construct_message(book_meta_data):
    summary = ''
    for s in book_meta_data['Summary']:
        summary += '<li>{}</li>'.format(s)

    template = '<h2><a href=\'{}\'>{}</a></h2>' \
               '<div>{}</div>' \
               '<div>{}</div>' \
               '<hr>' \
               '<img src=\'{}\' title=\'{}\'/>' \
               '<hr>' \
               '<p>Go <a href=\'{}\'>here</a>, login with your credentials and claim your free book</p>'\
        .format(book_meta_data['link'], book_meta_data['title'], book_meta_data['Description'], summary,
                book_meta_data['cover'], book_meta_data['title'], AFFLIATION_LINK, AFFLIATION_LINK)

    return template


def get_time_left(unix_time):
    end_time = datetime.fromtimestamp(int(unix_time))
    time_left = end_time - datetime.now()
    hrs, minutes, seconds = str(time_left).split(':')

    return "{} hours {} minutes".format(hrs, minutes)


if __name__ == "__main__":
    main()
