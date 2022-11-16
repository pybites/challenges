import os
import sys
import re

from datetime import datetime

DATETIME_REGEX = re.compile(r'.*(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}).*')
SHUTDOWN_EVENT = 'Shutdown initiated'

with open(os.path.join(sys.path[0], "messages.log"), "r") as f:
    loglines = f.readlines()


def convert_to_datetime(line):
    match = re.match(DATETIME_REGEX, line)
    return datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)),
                    int(match.group(5)), int(match.group(6))) if match else None


def time_between_shutdowns(loglines):
    start = None
    end = None
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            if dt := convert_to_datetime(line):
                if start:
                    end = dt
                else:
                    start = dt
    return end - start if end and start else None
