import argparse
from datetime import date, timedelta
import math

import schedule


class Resource:

    def __init__(self, title, comments_url, units, day_task, start=None):
        self.title = title.title()
        self.comments_url = comments_url
        self.units = int(units)
        self.day_task = int(day_task)
        self.num_days = math.ceil(self.units / self.day_task)
        self.start = start if start else date.today()
        self.end = self.start + timedelta(days=self.num_days)

    def get_daily_task(self):
        days = range(1, self.num_days + 1)
        for day in days:
            dt = self.start + timedelta(days=day)
            till = min(day * self.day_task, self.units)
            # self.unit_name (defined in child) magically works in parent
            yield '{} -> you will have completed: {} {} ({:.1f}%)'.format(
                    dt, till, self.unit_name, float(till)/self.units*100)

    def __str__(self):
        return ('Title: {title}\n'
                'comments_url: {comments_url}\n'
                'Planning: {num_days} days ({start} - {end})\n'
                '{unit_name}: {units} ({day_task} {unit_name}/day)'
               ).format(title=self.title,
                        comments_url=self.comments_url,
                        num_days=self.num_days,
                        start=self.start,
                        end=self.end,
                        unit_name=self.unit_name,
                        units=self.units,
                        day_task=self.day_task)


class Book(Resource):

    def __init__(self, title, comments_url, units, day_task, start=None):
        super().__init__(title, comments_url, units, day_task, start)

        # cool thing is I define this attribute on child but
        # can already use (plan for it) in parent!
        self.unit_name = 'pages'


class Video(Resource):

    def __init__(self, title, comments_url, units, day_task, start=None, hours=None):
        '''Default is minutes, but allow hours as optional arg on this child'''
        units = hours * 60 if hours else units
        super().__init__(title, comments_url, units, day_task, start)
        self.unit_name = 'minutes'

    # Could write other specialized methods for Video (as opposed to Resource / Book)


class Message:
    def __init__(self, resource, mails):
        self.res = resource
        if not isinstance(mails, list):
            raise TypeError('expecting list of emails')
        self.mails = list(mails)

    def send(self, task):
        subject = 'New Study Task: {} {} of {}'.format(
                self.res.day_task, self.res.unit_name, self.res.title)
        msg = ['Planning:']
        msg.append(str(self.res))
        msg.append('Task for today: ')
        msg.append(task)
        msg.append('Enjoy!')
        print()
        print('Subject: \n{}'.format(subject))
        print('\nBody: \n{}'.format('\n\n'.join(msg)))

        # TODO mail or SMS even?!


if __name__ == '__main__':
    '''
    # Book
    start = date.today() + timedelta(days=2)
    b = Book('superintelligence', 326, 10, start=start)
    print(b)
    for i in b.get_daily_task():
        print(i)

    print()

    # Video
    v = Video('data analysis', 0, 18, start=start, hours=3.4)
    print(v)
    for j in v.get_daily_task():
        print(j)
    '''

    # TODO: argparse to retrieve title, book/video, units (pages/min), emails

    start = date.today() + timedelta(days=2)
    resource = Book('superintelligence', 'http://osn.some.url.com', 326, 10, start=start)
    task_gen = resource.get_daily_task()

    mails = ['bob@gmail.com']
    m = Message(resource, mails)

    def job():
        task = next(task_gen)
        m.send(task)

    #schedule.every().day.at("10:30").do(job)
    for i in range(5):
        job()
        print('---\n')
