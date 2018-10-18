from collections import deque
import os
from time import sleep
import sys

import pyperclip
from termcolor import colored

MAX_CLIPBOARD_LEN = 10
SLEEP_INTERVAL = 3


class Clipper:

    def __init__(self, clips=None, interval=None):
        self._clips = clips and clips or deque(maxlen=MAX_CLIPBOARD_LEN)
        self._sleep = interval and interval or SLEEP_INTERVAL
        welcome = 'Welcome to Clipper! Press CTRL+C to retrieve a clip ...'
        print(colored(welcome, 'green'))
        print('-' * 80)

    def _sleep_and_clear(self):
        sleep(self._sleep)
        os.system('cls' if os.name == 'nt' else 'clear')

    def _update_clips(self):
        clip = pyperclip.paste()
        if clip not in self._clips:
            self._clips.append(clip)

    def _retrieve_clip(self):
        try:
            prompt = 'Enter clip number (press CTRL+C to exit): '
            selected = int(input(prompt))
            selected_clip = self._clips[selected-1]
            pyperclip.copy(selected_clip)
            print(colored(f'Copied "{selected_clip}" to clipboard\n', 'green'))
            self._sleep_and_clear()
        except(ValueError, KeyError):
            print(colored('Invalid clip, try again\n', 'red'))
            self._sleep_and_clear()
        except KeyboardInterrupt:
            self._exit()

    @property
    def clips(self):
        print('Clipper buffer:')
        print('-' * 80)
        for i, clip in enumerate(self._clips, 1):
            print(f'Clip #{i}\n{clip}\n')
        print(colored('\n-> press CTRL+C to retrieve a clip: ', 'magenta'))

    def _exit(self):
        print('\n')
        print('-' * 80)
        print(colored('Thanks for using Clipper, hope to cu soon!', 'green'))
        sys.exit(0)

    def __call__(self):
        while True:
            try:
                self._update_clips()
                self.clips
                self._sleep_and_clear()
            except KeyboardInterrupt:
                self._retrieve_clip()


if __name__ == '__main__':
    clipper = Clipper()
    clipper()
