import pygame
from pygame.rect import Rect

# scalar is used to scale time... it's the number of seconds for a
# pomodoro minute
scalar = 1
# pygame generic parameters
WIDTH, HEIGHT = 800, 300
FPS = 60

# pygame essentials
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Living with tomatoes')

# Pomodoro time periods
TIMES = {
    'work': 25,
    'rest': 5,
    'long_rest': 10
}
TIME_TRANSITIONS = {
    'work': ['rest', 'long_rest'],
    'rest': ['work'],
    'long_rest': ['work']
}
TIME_MESSAGES = {
    'work': 'Program! Program!',
    'rest': 'Cool your heels!',
    'long_rest': 'Get the coffee in!'
}
LONG_REST_AFTER = 3
pomodoro_status = 'work'
pomodoro_rest_count = 0

# timing elements
target_time = TIMES[pomodoro_status] * scalar
TIMER_STOPPED = 0
TIMER_RUNNING = 1
TIMER_PAUSED = 2
timer_status = TIMER_STOPPED

# colour setups
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)

# font declarations
BUTTON_FONT = pygame.font.SysFont('sans', 30)
TIMER_FONT = pygame.font.SysFont('sans', 100)
MESSAGE_FONT = pygame.font.SysFont('serif', 60)


# pomodoro specific declarations
def do_start():
    global timer_status
    if timer_status == TIMER_RUNNING:
        return
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    timer_status = TIMER_RUNNING


def do_pause():
    global timer_status
    if timer_status == TIMER_RUNNING:
        pygame.time.set_timer(pygame.USEREVENT, 0)
        timer_status = TIMER_PAUSED


def do_reset():
    global pomodoro_status, pomodoro_rest_count, target_time, timer_status
    if timer_status == TIMER_STOPPED:
        return
    pygame.time.set_timer(pygame.USEREVENT, 0)
    pomodoro_status = 'work'
    pomodoro_rest_count = 0
    target_time = TIMES[pomodoro_status] * scalar
    timer_status = TIMER_STOPPED


# buttons
BUTTONS = [
    ('START', (GREEN, GREY, GREEN), do_start),
    ('PAUSE', (GREY, BLUE, GREY), do_pause),
    ('RESET', (GREY, RED, RED), do_reset)
]
BUTTON_WIDTH, BUTTON_HEIGHT = 90, 40
BUTTON_COUNT = 3
GAP = 100
button_pos = []

# timer text
TICK_TEXT_CENTER = (WIDTH // 2, 75)
TICK_TEXT_COLOUR = RED


def init_button_positions():
    global button_pos

    button_left = (WIDTH - BUTTON_COUNT * BUTTON_WIDTH - GAP * (BUTTON_COUNT - 1)) // 2
    button_top = HEIGHT - round(BUTTON_HEIGHT * 1.5)
    for button in range(BUTTON_COUNT):
        button_pos.append(
            Rect(button_left + ((BUTTON_WIDTH + GAP) * button),
                 button_top,
                 BUTTON_WIDTH,
                 BUTTON_HEIGHT)
        )


def draw():
    display.fill(WHITE)
    # draw buttons
    for button in range(BUTTON_COUNT):
        rect = button_pos[button]
        pygame.draw.rect(display, BLACK, rect, 3)
        pygame.draw.rect(display, BUTTONS[button][1][timer_status], rect)
        text = BUTTON_FONT.render(BUTTONS[button][0], 1, WHITE)
        display.blit(text,
                     (rect.centerx - text.get_width() // 2,
                      rect.centery - text.get_height() // 2))
    text = TIMER_FONT.render(f'{target_time // 60}:{target_time % 60:02}', 1, TICK_TEXT_COLOUR)
    display.blit(text,
                 (TICK_TEXT_CENTER[0] - text.get_width() // 2,
                  TICK_TEXT_CENTER[1] - text.get_height() // 2))
    offset = text.get_height()
    if timer_status == TIMER_RUNNING:
        text = MESSAGE_FONT.render(TIME_MESSAGES[pomodoro_status], 1, BLACK)
    elif timer_status == TIMER_PAUSED:
        text = MESSAGE_FONT.render("This isn't right you know!", 1, RED)
    else:
        text = MESSAGE_FONT.render('Waiting…', 1, GREEN)
    display.blit(text,
                 (TICK_TEXT_CENTER[0] - text.get_width() // 2,
                  TICK_TEXT_CENTER[1] + offset - text.get_height() // 2))
    pygame.display.update()


def main():
    init_button_positions()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for n, button in enumerate(button_pos):
                    if button.collidepoint(pos):
                        (BUTTONS[n][2])()
            if event.type == pygame.USEREVENT:
                global target_time, pomodoro_status, pomodoro_rest_count
                target_time -= 1 if target_time > 0 else 0
                if target_time == 0:
                    transition = TIME_TRANSITIONS[pomodoro_status]
                    if len(transition) == 1:
                        pomodoro_status = transition[0]
                    else:
                        if pomodoro_rest_count == LONG_REST_AFTER:
                            pomodoro_status = transition[1]
                            pomodoro_rest_count = 0
                        else:
                            pomodoro_status = transition[0]
                            pomodoro_rest_count += 1
                    target_time = TIMES[pomodoro_status]

    pygame.quit()


if __name__ == '__main__':
    main()
