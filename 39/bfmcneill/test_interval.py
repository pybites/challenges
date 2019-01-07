from unittest.mock import patch
from datetime import datetime
from time import sleep

import pytest

from interval import Interval, datetime_round, interval_states


def test_round_down():
    dt = datetime(2018, 12, 30, 4, 5, 6, 480000)
    expected = datetime_round(dt)
    assert expected == datetime(2018, 12, 30, 4, 5, 6)


def test_round_up():
    dt = datetime(2018, 12, 30, 4, 5, 6, 580000)
    expected = datetime_round(dt)
    assert expected == datetime(2018, 12, 30, 4, 5, 7)


def test_interval_status_initial():
    interval = Interval()
    assert interval.status == interval_states["INITIAL"]


def test_interval_status_active():
    interval = Interval()
    interval.begin()
    assert interval.status == interval_states["ACTIVE"]


def test_interval_status_complete():
    interval = Interval()
    interval.begin()
    interval.expire()
    assert interval.status == interval_states["COMPLETE"]


def test_interval_begin_while_in_process():
    interval = Interval()
    interval.begin()
    with pytest.raises(ValueError):
        interval.begin()


def test_interval_expire_before_begin():
    interval = Interval()
    with pytest.raises(ValueError):
        interval.expire()


def test_interval_begin_a_completed_process():
    interval = Interval()
    interval.begin()
    interval.expire()
    with pytest.raises(ValueError):
        interval.begin()


def test_interval_duration_mid_process():
    interval = Interval()
    interval.begin()
    with pytest.raises(ValueError):
        interval.durration_calc()


def test_interval_durration():
    interval = Interval()
    interval.begin()
    sleep(1.1)
    interval.expire()
    assert interval.durration_calc() == 1
