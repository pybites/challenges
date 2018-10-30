#!/usr/bin/env python
import datetime
import glob
import os
import re
import subprocess
import sys

HOME = os.path.expanduser("~")
FFMPEG = os.path.join(HOME, 'bin', 'ffmpeg')
EXTENSIONS = ('mp3', 'mp4', 'm4a')


def _get_duration(video):
    command = [FFMPEG, "-i", video, "2>&1"]
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return str(pipe.communicate()[0])


def _convert_to_seconds(output):
    timestamp = re.sub(r'.*Duration: (\d{2}:\d{2}:\d{2}).*', r'\1', output)
    try:
        hours, minutes, seconds = timestamp.split(':')
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    except ValueError:
        return 0


def get_video_duration_in_seconds(video):
    output = _get_duration(video)
    return _convert_to_seconds(output)


def _get_total_duration(durations):
    total = datetime.timedelta(seconds=0)
    # noice! https://stackoverflow.com/a/2780979
    for duration in durations:
        total += datetime.timedelta(seconds=duration)
    return str(total)


def _get_video_number(video):
    filename = os.path.basename(video)
    try:
        return int(re.split(r'[-_]', filename)[0])
    except ValueError:
        return filename


def get_lesson_duration(lesson_dir, silent=False, int_sort=False):
    videos = glob.glob(os.path.join(lesson_dir, f'*{["|".join(EXTENSIONS)]}'))

    # if filenames start with an int followed by - or _, sort on that int
    if int_sort:
        videos.sort(key=_get_video_number)

    durations = [get_video_duration_in_seconds(video)
                 for video in videos
                 if video.endswith(EXTENSIONS)]

    total = _get_total_duration(durations)

    if not silent:
        for vid, duration in zip(videos, durations):
            print(f'{os.path.basename(vid):<40}: {duration}')
        print('-'*50)
        print(f'{"Total":<40}: {total}')

    return total


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} PATH_WITH_MP4_FILES')
        sys.exit(1)

    dirname = sys.argv[1]
    if not os.path.isdir(dirname):
        print('Not a valid directory')
        sys.exit(1)

    get_lesson_duration(dirname, silent=False, int_sort=True)
