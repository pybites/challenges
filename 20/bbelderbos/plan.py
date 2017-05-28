from datetime import date, timedelta
import math
import os
import sys
import time

import click
import schedule
from twilio.rest import Client

ACCOUNT_SID = (os.environ.get('TWILIO_SID') or
               sys.exit('need account sid'))
AUTH_TOKEN = (os.environ.get('TWILIO_TOK') or
              sys.exit('need auth token'))
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
FROM_PHONE = (os.environ.get('TWILIO_PHONE') or
              sys.exit('need Twilio (verified) phone'))


class Resource:

    def __init__(self, title, units, day_task, start=None):
        self.title = title.title()
        self.units = int(units)
        self.day_task = int(day_task)
        self.num_days = math.ceil(self.units / self.day_task)
        self.start = start if start else date.today()
        self.end = self.start + timedelta(days=self.num_days)
        self.tasks = self._get_daily_task()

    def _get_daily_task(self):
        days = range(1, self.num_days + 1)
        for day in days:
            dt = self.start + timedelta(days=day)
            till = min(day * self.day_task, self.units)
            yield '{} goal: reach {} {} ({:.1f}% done)'.format(
                  dt, till, self.unit_name,
                  float(till)/self.units*100)

    def __str__(self):
        return ('Title: {title}\n'
                'Planning: {num_days} days ({start} - {end})\n'
                'Total: {unit_name}: {units} '
                '(speed: {day_task} {unit_name}/day)').format(
                title=self.title,
                num_days=self.num_days,
                start=self.start,
                end=self.end,
                unit_name=self.unit_name,
                units=self.units,
                day_task=self.day_task)


class Book(Resource):

    def __init__(self, title, units, day_task, start=None):
        super().__init__(title, units, day_task, start)

        # cool: defined attribute child, but also using it in parent
        self.unit_name = 'pages'


class Video(Resource):

    def __init__(self, title, units,
                 day_task, start=None):
        super().__init__(title, units, day_task, start)
        self.unit_name = 'minutes'

    # future specialized methods ...


def send_sms(res, task, to_phones):
    sids = []
    for phone in to_phones:
        message = CLIENT.messages.create(
            from_=FROM_PHONE,
            to=phone,
            body=task
        )
        sids.append(message.sid)
    return sids


@click.command()
@click.option('--resource', help='resource type (book, video)')
@click.option('--title', help='title of resource')
@click.option('--total_units',
              help='total units resource (book = pages, video = min)')
@click.option('--units_per_day',
              help='total units (book = pages, video = min) per day')
@click.option('--start_in_days',
              help='number of days from now we kick this off (optional)',
              required=False)
@click.option('--to_phones', help='list of phone numbers to notify')
def main(resource, title, total_units,
         units_per_day, start_in_days, to_phones):

    if start_in_days:
        start_date = date.today() + timedelta(days=int(start_in_days))
    else:
        start_date = date.today()

    to_phones = to_phones.split()

    resource = resource.lower()
    if resource == 'book':
        Resource_ = Book
    elif resource == 'video':
        Resource_ = Video
    else:
        raise ValueError('What resource? I know about Book and Video')

    resource = Resource_(title, total_units,
                         units_per_day, start=start_date)
    print(resource)
    print()

    def job():
        try:
            task = next(resource.tasks)
        except StopIteration:
            print('Resource done')
            sys.exit(0)
        print(task)
        send_sms(resource, task, to_phones)

    schedule.every().day.at("8:00").do(job)
    # replace line for quick test
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
