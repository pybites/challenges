from tkinter import *
from datetime import timedelta
import time
from copy import copy

dt = timedelta(minutes=25)
default_time = copy(dt)
after_id = ''

def set_up(event):
    global default_time
    try:
        default_time = timedelta(minutes=int(entry_set_up.get()))
    except:
        pass

    label1.configure(text=':'.join(str(default_time).split(':')[1:]))

def timer():
    global after_id, default_time
    after_id = root.after(1000, timer)
    if default_time.seconds == 0:
        time.sleep(2)
        stop_timer()
        reset_timer()
    label1.configure(text=':'.join(str(default_time).split(':')[1:]))
    default_time -= timedelta(seconds=1)

def start_timer():
    btn_start.grid_forget()
    entry_set_up.grid_forget()
    btn_set_up.grid_forget()
    btn_stop.grid(row=2, columnspan=2, sticky='ew')
    timer()

def stop_timer():
    btn_stop.grid_forget()
    btn_continue.grid(row=2, column=0, sticky='ew')
    btn_reset.grid(row=2, column=1, sticky='ew')
    root.after_cancel(after_id)

def continue_timer():
    btn_continue.grid_forget()
    btn_reset.grid_forget()
    btn_stop.grid(row=2, columnspan=2, sticky='ew')
    timer()

def reset_timer():
    global default_time, after_id, dt
    default_time = copy(dt)
    label1.configure(text=':'.join(str(default_time).split(':')[1:]))
    btn_continue.grid_forget()
    btn_reset.grid_forget()
    btn_start.grid(row=2, columnspan=2, sticky='ew')
    entry_set_up.grid(row=1, column=0, sticky='e')
    btn_set_up.grid(row=1, column=1, sticky='we')

root = Tk()
root.title('Pomodoro Timer')

label1 = Label(root, width=5, text=':'.join(str(default_time).split(':')[1:]), font=('Arial', 100))
label1.grid(row=0, columnspan=2)

label_set_up = Label(root, width=5, text='Minutes', font=('Arial', 15))
label_set_up.grid(row=1, column=0, sticky='we')

entry_set_up = Entry(root, width=3, font=15)
entry_set_up.grid(row=1, column=0, sticky='e')

btn_set_up = Button(root, text='Set Up', font=('Arial', 15))
btn_set_up.grid(row=1, column=1, sticky='we')
btn_set_up.bind('<Button-1>', set_up)

btn_start = Button(root, text='Start', font=('Arial', 30), command=start_timer)
btn_stop = Button(root, text='Stop', font=('Arial', 30), command=stop_timer)
btn_continue = Button(root, text='Continue', font=('Arial', 30), command=continue_timer)
btn_reset = Button(root, text='Reset', font=('Arial', 30), command=reset_timer)

btn_start.grid(row=2, columnspan=2, sticky='ew')

root.mainloop()