from collections import Counter
from datetime import datetime, date
import glob
import os
import re

from git import Repo

BLOG_DIR = 'pybites-blog'
MD_FILES = glob.glob(os.path.join(BLOG_DIR, 'content', '*md'))

if not os.path.isdir(BLOG_DIR):
    Repo.clone_from('https://github.com/pybites/pybites.github.io-src',
                    BLOG_DIR)


def _extract_date(lines):
    '''Helper to locate the Date meta field and extract date string
       from it converting it to a proper datetime'''
    for line in lines:
        m = re.search(r'^Date:\s(.*)', line)
        if m:
            date_str = m.groups()[0]
            dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
            return dt
    return None


def _count_words(md_file):
    '''Count words in md file, discarding meta data'''
    with open(md_file) as f:
        lines = [li.strip() for li in f.readlines()]

        # ignore meta data
        date = _extract_date(lines)

        if not date:
            return None, None

        words = sum(len(line.split())
                    for line in lines
                    if line.strip() and not re.search(r'^\S+:\s', line))

        return date, words


def get_word_counts_per_month(md_files=MD_FILES):
    '''Loops over all md files and keeps counter of words per month
       sorts by keys (months) and returns 2 lists: x_values = months,
       y_values = word_counts'''
    counter = Counter()
    for md_file in md_files:
        dt, words = _count_words(md_file)

        if dt is None:
            continue

        dt_truncated = date(dt.year, dt.month, dt.day)
        counter[dt_truncated] += words

    counter_sorted = sorted(counter.items())
    x_values, y_values = zip(*counter_sorted)

    return x_values, y_values


if __name__ == '__main__':
    x_values, y_values = get_word_counts_per_month()

    print('x_values:', x_values)
    print('y_values:', y_values)
