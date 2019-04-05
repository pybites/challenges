#!/usr/bin/env python
from collections import Counter
from datetime import datetime, timedelta
from operator import itemgetter
import os
from random import randint
import sqlite3
import sys

import easygui as g
import matplotlib.pyplot as plt
import numpy as np

DB = 'pomodoro.db'
OPTIONS = ['Add pomodoro', 'Add multiple pomodori',
           'Show pomodori', 'Reset', 'Exit']
POMODORI_AMOUNTS = range(1, 6)
POMODORO_IMG = 'pomodoro.png'
STATS_IMG = 'stats.png'
WEEKLY_GOAL = 7
PLOT_TITLE = 'Reading progress (weekly goal = {} pomodori)'.format(WEEKLY_GOAL)


class PomodoriLogger:

    def __init__(self, fake_data):
        self.conn = sqlite3.connect(DB, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs
                               (date timestamp, pomodori integer)''')

        if fake_data:
            self._insert_fake_pomos()

        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def _insert_fake_pomos(self):
        self.cursor.execute('SELECT * FROM logs')
        row = self.cursor.fetchone()
        if row is not None:
            return

        for i in range(7, 71, 7):
            date = datetime.now() - timedelta(days=i)
            amount = randint(1, 10)
            self.cursor.execute('INSERT INTO logs VALUES(?, ?)', (date,
                                                                  amount))
        self.conn.commit()

    def add_pomodori(self, amount=1):
        try:
            amount = int(amount)
        except ValueError:
            raise

        if amount not in POMODORI_AMOUNTS:
            raise ValueError('Amount not in {}'.format(str(POMODORI_AMOUNTS)))

        date = datetime.now()
        self.cursor.execute('INSERT INTO logs VALUES(?, ?)', (date, amount))
        self.conn.commit()

    def reset(self):
        self.cursor.execute('DELETE FROM logs')
        self.conn.commit()

    def _calc_stats(self):
        stats = Counter()
        for row in self.cursor.execute('SELECT * FROM logs'):
            dt = row[0]
            amount = row[1]
            isocal = dt.isocalendar()
            year = isocal[0]
            week = str(isocal[1]).zfill(2)
            year_week = '{}-{}'.format(year, week)
            stats[year_week] += amount
        return stats

    def _get_colors(self, pomodori):
        colors = []
        for pomo in pomodori:
            if pomo >= WEEKLY_GOAL:
                colors.append('g')
            else:
                colors.append('r')
        return colors

    def _make_graph(self, stats):
        stats_sorted = sorted(stats.items(), key=itemgetter(0))

        weeks = [p[0] for p in stats_sorted]
        y_pos = np.arange(len(weeks))
        pomodori = [p[1] for p in stats_sorted]

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # https://stackoverflow.com/a/3833007/1128469
        colors = self._get_colors(pomodori)

        ax.barh(y_pos, pomodori, align='center',
                color=colors, ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(weeks)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Pomodori')
        ax.set_title(PLOT_TITLE)

        fig.set_size_inches(7.6, 3.8)
        plt.savefig(STATS_IMG)
        # to avoid '_tkinter.TclError: image "pyimage.." doesn't exist'
        plt.close()

    def show_stats(self):
        stats = self._calc_stats()
        self._make_graph(stats)
        g.buttonbox('', image=STATS_IMG, choices=['Go back'])


def main(fake_data):
    with PomodoriLogger(fake_data) as pomo:

        while True:
            action = g.indexbox('', image=POMODORO_IMG, choices=OPTIONS)

            if action == 0:
                pomo.add_pomodori()

            elif action == 1:
                num_pomos = g.choicebox('How many pomodori?',
                                        'Input amount of pomodori',
                                        POMODORI_AMOUNTS)
                pomo.add_pomodori(num_pomos)

            elif action == 2:
                pomo.show_stats()

            elif action == 3:
                msg = "Do you want to continue?"
                title = "Please Confirm"
                if g.ccbox(msg, title):
                    pomo.reset()

            elif action == 4:
                print('Goodbye')
                sys.exit(0)

            else:
                print('Invalid choice')
                continue


if __name__ == '__main__':
    fake_data = False

    if len(sys.argv) > 1:
        args = sys.argv[1:]

        if '-f' in args:
            fake_data = True

        if '-r' in args and os.path.isfile(DB):
            os.remove(DB)

    main(fake_data)
