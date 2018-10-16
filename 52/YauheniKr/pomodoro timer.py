from datetime import timedelta
import time



def timer_func(pomodoro_timer):
    pomodoro_timer = timedelta(minutes=pomodoro_timer)
    while pomodoro_timer != timedelta(seconds=0):
        time.sleep(1)
        pomodoro_timer -= timer_delta
        print(pomodoro_timer)



while True:
    pomodoro_timer = int(input('Введите таймер помидора, мин'))
    cycle_number = int(input('Введите число таймеров помидора'))
    pomodoro_break = int(input('Введите таймер отдыха между таймерами помидора, мин'))
    cycle_break = int(input('Введите время отдыха между циклами, мин'))
    timer_delta = timedelta(seconds=1)
    while cycle_number > 0:
        print('Время поработать.')
        timer_func(pomodoro_timer)
        cycle_number -= 1
        if cycle_number == 0:
            print('Цикл закончился. Запускаем таймер отдыха между циклами')
            timer_func(cycle_break)
        else:
            print('Таймер помидора закончился, пора сделать перерыв.')
            timer_func(pomodoro_break)
    cont_cycle = input('Цикл помидора закончился. Желаете продолжить работать, Да/Нет')
    if cont_cycle == 'Да':
        continue
    else:
        break