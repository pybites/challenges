from datetime import date, timedelta

import pytest

from plan import Book, Video

TODAY = date(2017, 5, 29)

book1 = Book('superintelligence', 328, 10, 
             start=TODAY)
book2 = Book('4HWW', 416, 20,
             start=TODAY+timedelta(days=7))
video1 = Video('Effective Data Analysis Using Python',
               11*60, 30,
               start=TODAY+timedelta(days=4))

book1_tasks = list(book1.tasks)
book2_tasks = list(book2.tasks)
video1_tasks = list(video1.tasks)


def test_number_of_days():
    assert len(book1_tasks) == 33
    assert len(book2_tasks) == 21
    assert len(video1_tasks) == 22


def test_task_descriptions():
    assert book1_tasks[0] == \
           '2017-05-29 goal: reach 10 pages (3.0% done)'
    assert book1_tasks[-1] == \
           '2017-06-30 goal: reach 328 pages (100.0% done)'
    assert book2_tasks[0] == \
           '2017-06-05 goal: reach 20 pages (4.8% done)'
    assert book2_tasks[-1] == \
           '2017-06-25 goal: reach 416 pages (100.0% done)'
    assert video1_tasks[0] == \
           '2017-06-02 goal: reach 30 minutes (4.5% done)'
    assert video1_tasks[-1] == \
           '2017-06-23 goal: reach 660 minutes (100.0% done)'


if __name__ == '__main__':
    pytest.main()
