from collections import Counter
import datetime
import sqlite3
import sys

import easygui as g

POMODORI_AMOUNTS = range(1, 6)
OPTIONS = ['Log pomodori', 'Show stats', 'Exit']
POMODORO_IMG = 'pomodoro.gif'
POMODORO_MIN = 25
TOMATO_CHAR = u'\U0001F345'
TOMATE_SAFE_CHAR = u'\U+1F345'
print(TOMATE_SAFE_CHAR)
sys.exit()


class PomodoriLogger:

    def __init__(self):
        self.conn = sqlite3.connect('pomodoro.db',
                                    detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS logs
                               (date timestamp, pomodori integer)''')
        self.conn.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def add_pomodori(self, amount=1):
        try:
            amount = int(amount)
        except ValueError:
            raise

        if amount not in POMODORI_AMOUNTS:
            raise ValueError('Amount not in {}'.format(str(POMODORI_AMOUNTS)))

        date = datetime.datetime.now()
        self.cursor.execute('INSERT INTO logs VALUES(?, ?)', (date, amount))
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

    def show_stats(self):
        stats = self._calc_stats()
        fmt = '{:<7} | {}'
        divider = '-' * 80

        header = fmt.format('Week', 'Pomodori')
        print(header)
        print(divider)

        output = [header]
        output.append(divider)

        for week, num_pomos in stats.items():
            pomo_symbol = TOMATO_CHAR + ' '
            pomodori = num_pomos * pomo_symbol
            line = fmt.format(week, pomodori)

            # unicode does not work in tcl :(
            # can print it to stdout though :)
            print(line)
            line = line.replace(TOMATO_CHAR, TOMATE_SAFE_CHAR)
            output.append(line)

        # text- and codebox give input field, I just want display only
        g.buttonbox('\n'.join(output), image=POMODORO_IMG, choices=['Go back'])


def main():
    with PomodoriLogger() as pomo:

        while True:
            action = g.indexbox('', image=POMODORO_IMG, choices=OPTIONS)

            if action == 0:
                num_pomos = g.choicebox('How many pomodori?',
                                        'Input amount of pomodori',
                                        POMODORI_AMOUNTS)
                pomo.add_pomodori(num_pomos)

            elif action == 1:
                pomo.show_stats()

            elif action == 2:
                print('Goodbye')
                sys.exit(0)

            else:
                print('Invalid choice')
                continue


if __name__ == '__main__':
    main()
