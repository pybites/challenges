from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('http://pyplanet.herokuapp.com/')


if __name__ == '__main__':
    main()
