"""
test_pomodoro_timer.py

Tests for pomodoro_timer.
"""
import logging
from unittest.mock import patch

import pytest

from pomodoro_timer import app

logging.disable(logging.CRITICAL)


@pytest.fixture()
def timer():
    test_app = app.Pomodoro(1, breaks=1, interval=2)
    return test_app


def test_class_initialization(timer):
    assert timer.p_duration == 3600
    assert timer.p_breaks == 60
    assert timer.p_interval == 120
    assert timer.status == "IDLE"
    assert timer.rounds == 1


def test_start_interval(capfd, timer):
    timer.start_interval()
    output = capfd.readouterr()[0]
    assert "Next break" in output
    assert timer.status == "ACTIVE"
    assert timer.rounds == 2


def test_start_break(capfd, timer):
    timer.start_break()
    output = capfd.readouterr()[0]
    assert "Start again at" in output
    assert timer.status == "RESPITE"


def test_done_alarm(timer):
    timer.play("done")
    pass


def test_repr(timer):
    assert repr(timer) == "Pomodoro(duration:1 breaks=1 interval=2)"


def test_bye_message(capfd, timer):
    with pytest.raises(SystemExit):
        timer.bye_message()
    output = capfd.readouterr()[0]
    assert output.strip() == "Thanks for using clamytoe's Pomodoro Timer!"


@patch("builtins.input", side_effect=["", 4, "y", "q"])
def test_get_input_continue(inp):
    timer = app.Pomodoro(1, breaks=1, interval=2)
    assert timer.get_input() is None
    assert timer.get_input() is None
    assert timer.get_input() is None
    with pytest.raises(SystemExit):
        timer.get_input()


@patch("builtins.input", side_effect=[""])
def test_pause(capfd, timer):
    assert timer.pause(1) is None
