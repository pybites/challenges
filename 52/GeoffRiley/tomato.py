"""
     🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅
    🍅   Pomodoro Timer  🍅
     🍅 🍅 🍅 🍅 🍅 🍅 🍅 🍅
"""
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Tuple

import pygame
import pygame.freetype
import math
from pygame.rect import Rect

# scalar is used to scale time... it's the number of seconds for a
# pomodoro minute: normal is 60 for real time; testing is 1 for fast time
scalar = 1
# pygame generic parameters
WIDTH, HEIGHT = 700, 300
FPS = 50

# colour setups
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)


class TimerStatus(Enum):
    TIMER_STOPPED = 0
    TIMER_RUNNING = 1
    TIMER_PAUSED = 2


@dataclass
class Point:
    x: int
    y: int

    @property
    def xy(self) -> Tuple[int, int]:
        return self.x, self.y


# timer text
TICK_TEXT_CENTER = Point(WIDTH // 2, 75)
TICK_TEXT_COLOUR = RED


@dataclass
class PomButton:
    text: str
    colour_map: Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]
    action: Callable[[], None]
    button_pos: Point
    width: int = 90
    height: int = 40

    def colour_for_status(self, status: TimerStatus) -> Tuple[int, int, int]:
        return self.colour_map[status.value]

    def collidepoint(self, pos: Tuple[int, int]):
        if self.rect.collidepoint(pos[0], pos[1]):
            self.action()

    @property
    def rect(self):
        return Rect(self.button_pos.xy, (self.width, self.height))


class Pomodoro:
    # buttons
    BUTTON_COUNT = 3
    BUTTON_WIDTH, BUTTON_HEIGHT = 90, 40
    BUTTON_GAP = 100
    buttons = []

    def __init__(self, work: int = 25, rest: int = 5, long_rest: int = 10):
        # pygame essentials
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Living with tomatoes')
        self.TIMES = {
            'work': work,
            'rest': rest,
            'long_rest': long_rest
        }
        self.TIME_TRANSITIONS = {
            'work': ['rest', 'long_rest'],
            'rest': ['work'],
            'long_rest': ['work']
        }
        self.TIME_MESSAGES = {
            'work': 'Program! Program!',
            'rest': 'Cool your heels!',
            'long_rest': 'Get the coffee in!'
        }
        self.long_rest_after = 3
        self.pomodoro_status = 'work'
        self.pomodoro_rest_count = 0

        # timing elements
        self.target_time = self.TIMES[self.pomodoro_status] * scalar
        self.timer_status = TimerStatus.TIMER_STOPPED
        self.timer_start = self.target_time

        # font declarations
        self.BUTTON_FONT = pygame.freetype.SysFont('sans', 30)
        self.TIMER_FONT = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 100)
        self.MESSAGE_FONT = pygame.freetype.SysFont('serif', 60)

        # clock representation
        self.clock_rect = Rect(10, 30, 80, 80)

    def do_start(self):
        if self.timer_status == TimerStatus.TIMER_RUNNING:
            return
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.timer_status = TimerStatus.TIMER_RUNNING

    def do_pause(self):
        if self.timer_status == TimerStatus.TIMER_RUNNING:
            pygame.time.set_timer(pygame.USEREVENT, 0)
            self.timer_status = TimerStatus.TIMER_PAUSED

    def do_reset(self):
        if self.timer_status == TimerStatus.TIMER_STOPPED:
            return
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.pomodoro_status = 'work'
        self.pomodoro_rest_count = 0
        self.target_time = self.TIMES[self.pomodoro_status] * scalar
        self.timer_status = TimerStatus.TIMER_STOPPED
        self.timer_start = self.target_time

    def init_button_positions(self):
        button_left = (WIDTH - self.BUTTON_COUNT * self.BUTTON_WIDTH -
                       self.BUTTON_GAP * (self.BUTTON_COUNT - 1)) // 2
        button_top = HEIGHT - round(self.BUTTON_HEIGHT * 1.5)
        button_pos = []
        for button in range(self.BUTTON_COUNT):
            button_pos.append(
                Point(button_left + ((self.BUTTON_WIDTH + self.BUTTON_GAP) * button),
                      button_top)
            )
        self.buttons.extend([
            PomButton('START', (GREEN, GREY, GREEN), self.do_start, button_pos[0]),
            PomButton('PAUSE', (GREY, BLUE, GREY), self.do_pause, button_pos[1]),
            PomButton('RESET', (GREY, RED, RED), self.do_reset, button_pos[2])
        ])

    def draw(self):
        self.display.fill(WHITE)
        # draw buttons
        for button_id in range(self.BUTTON_COUNT):
            button = self.buttons[button_id]
            rect = button.rect  # self.button_pos[button_id]
            pygame.draw.rect(self.display, BLACK, rect, 3)
            pygame.draw.rect(self.display, button.colour_for_status(self.timer_status), rect)
            text = self.BUTTON_FONT.render(button.text, WHITE)
            self.display.blit(text[0],
                              (rect.centerx - text[1].width // 2,
                               rect.centery - text[1].height // 2))
        #  draw countdown
        text = self.TIMER_FONT.render(f'{self.target_time // 60}:{self.target_time % 60:02}',
                                      TICK_TEXT_COLOUR)
        self.display.blit(text[0],
                          (TICK_TEXT_CENTER.x - text[1].width // 2,
                           TICK_TEXT_CENTER.y - text[1].height // 2))
        offset = text[1].height
        if self.timer_status == TimerStatus.TIMER_RUNNING:
            text = self.MESSAGE_FONT.render(self.TIME_MESSAGES[self.pomodoro_status], BLACK)
        elif self.timer_status == TimerStatus.TIMER_PAUSED:
            text = self.MESSAGE_FONT.render("This isn't right you know!", RED)
        else:
            text = self.MESSAGE_FONT.render('Waiting…', GREEN)
        self.display.blit(text[0],
                          (TICK_TEXT_CENTER.x - text[1].width // 2,
                           TICK_TEXT_CENTER.y + offset - text[1].height // 2))

        # draw timer pie
        if self.target_time > 0:
            pygame.draw.arc(self.display,
                            RED if self.pomodoro_status == 'work' else BLUE,
                            self.clock_rect,
                            math.radians(90-(360/(self.timer_start/self.target_time))),
                            math.radians(90),
                            5)
        if self.pomodoro_rest_count < self.long_rest_after:
            pygame.draw.arc(self.display,
                            GREEN,
                            self.clock_rect.inflate(-14, -14),
                            math.radians(90-(360/(self.long_rest_after/(self.long_rest_after-self.pomodoro_rest_count)))),
                            math.radians(90),
                            5)

        pygame.display.update()

    def next_transition(self):
        transition = self.TIME_TRANSITIONS[self.pomodoro_status]
        if len(transition) == 1:
            self.pomodoro_status = transition[0]
        else:
            if self.pomodoro_rest_count == self.long_rest_after:
                self.pomodoro_status = transition[1]
                self.pomodoro_rest_count = 0
            else:
                self.pomodoro_status = transition[0]
                self.pomodoro_rest_count += 1
        self.target_time = self.TIMES[self.pomodoro_status]
        self.timer_start = self.target_time

    def main(self):
        self.init_button_positions()
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        button.collidepoint(pos)
                if event.type == pygame.USEREVENT:
                    self.target_time -= 1 if self.target_time > 0 else 0
                    if self.target_time == 0:
                        self.next_transition()
        pygame.quit()


if __name__ == '__main__':
    pom = Pomodoro()
    pom.main()
