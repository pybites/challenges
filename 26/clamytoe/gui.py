# -*- coding: utf-8 -*-
import tkinter as tk
# from tkinter import ttk
from tkinter import Menu, ttk

from pytrack import get_active, get_projects, get_selected, STATE
from pytrack import select_project, start_tracking, stop_tracking
from pytrack import add_project, remove_project

__version__ = '0.2.0'
__author__ = 'Martin Uribe'

PROJECTS = None
SELECTED_PROJECT = None
ACTIVE_PROJECT = None
PROJECT_NAMES = None
INDEX = None
TABS = None
TAB_1 = None
TAB_2 = None
TAB_3 = None
TAB_4 = None


# global variables
def init_globals():
    global PROJECTS, SELECTED_PROJECT, ACTIVE_PROJECT, PROJECT_NAMES, INDEX
    PROJECTS = get_projects()

    if PROJECTS:
        SELECTED_PROJECT = get_selected()
        ACTIVE_PROJECT = get_active()
        PROJECT_NAMES = [project.name for project in PROJECTS]
        INDEX = PROJECTS.index(SELECTED_PROJECT)


def main():
    """Assemble the GUI"""
    global TAB_1, TAB_2, TAB_3, TAB_4, TABS
    init_globals()

    # create window instance
    win = tk.Tk()
    win.title('Time Tracker')

    # tabs
    TABS = ttk.Notebook(win)

    TAB_1 = ttk.Frame(TABS)
    TAB_2 = ttk.Frame(TABS)
    TAB_3 = ttk.Frame(TABS)
    TAB_4 = ttk.Frame(TABS)
    TABS.add(TAB_1, text='Main')
    TABS.add(TAB_2, text='Add')
    TABS.add(TAB_3, text='Remove')
    TABS.add(TAB_4, text='About')
    TABS.pack(expand=1, fill='both')

    # setup_menu(win)
    setup_tab1(TAB_1)
    setup_tab4(TAB_4)

    # detect when the user switches between the tabs
    def tab_switch(event):
        if event.widget.identify(event.x, event.y) == 'label':
            index = event.widget.index('@%d, %d' % (event.x, event.y))
            title = event.widget.tab(index, "text")

            # only way I found to reload the tabs is to recreate them :(
            if title == 'Main':
                if not ACTIVE_PROJECT:
                    init_globals()
                    setup_tab1(TAB_1)
            elif title == 'Add':
                init_globals()
                setup_tab2(TAB_2)
            elif title == 'Remove':
                init_globals()
                setup_tab3(TAB_3)

    TABS.bind('<Button-1>', tab_switch)
    TABS.pack(fill='both', expand=True)

    # disable resizing
    win.resizable(0, 0)

    # try to keep on top
    win.wm_attributes('-topmost', 1)

    # start application
    win.mainloop()


def setup_menu(win):
    # menu bar commands
    def _quit():
        win.quit()
        win.destroy()
        exit()

    # menu bar
    menu_bar = Menu(win)
    win.config(menu=menu_bar)

    # file menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Add Project...')
    file_menu.add_command(label='Remove Project...')
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=_quit)
    menu_bar.add_cascade(label='File', menu=file_menu)

    # help menu
    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='About')
    menu_bar.add_cascade(label='Help', menu=help_menu)


def setup_tab1(tab):
    # global ACTIVE_PROJECT
    button_label = set_lable()

    # main frame
    main_frame = ttk.LabelFrame(tab, text='Project')
    main_frame.grid(columnspan=2, row=0, padx=5, pady=5, sticky='ew')

    project_choice = tk.StringVar()

    project_choices = ttk.Combobox(main_frame, width=18, textvariable=project_choice, state='readonly')
    project_choices['values'] = PROJECT_NAMES
    project_choices.grid(columnspan=2, row=0, padx=5, pady=5)
    project_choices.current(INDEX) if PROJECTS else project_choices.set('')
    project_choices.configure(state='disabled') if ACTIVE_PROJECT else project_choices.configure(state='enabled')
    project_choices.configure(state='enabled') if PROJECTS else project_choices.configure(state='disabled')

    # info
    info_label = ttk.Label(main_frame, text='')
    info_label.grid(column=0, row=1, padx=5, pady=5)
    info = ttk.Label(main_frame, text='')
    info.grid(column=1, row=1, padx=5, pady=5)

    # let user know if there are no projects
    if not PROJECTS:
        info_label.configure(text='Projects:')
        info.configure(text='None')

    # font color
    info.configure(foreground=get_color())

    # add buttons and code
    def select_command():
        """Make project selection"""
        global INDEX, SELECTED_PROJECT
        project = PROJECTS[PROJECT_NAMES.index(project_choice.get())]
        select_project(project.id)
        SELECTED_PROJECT = get_selected()
        INDEX = PROJECTS.index(SELECTED_PROJECT)
        action_button.configure(state='enabled')
        info_label.configure(text='Total:')
        info.configure(text=SELECTED_PROJECT.duration)
        update_win()

    def start_stop_command():
        """Start/Stop tracking depending on project status"""
        global ACTIVE_PROJECT, INDEX, SELECTED_PROJECT

        if ACTIVE_PROJECT:
            stop_tracking()
            project_choices.configure(state='enabled')
            select_button.configure(state='enabled')
            info_label.configure(text='Worked:')
            SELECTED_PROJECT = get_selected()
            info.configure(text=SELECTED_PROJECT.duration)
            TABS.tab(1, state='normal')
            TABS.tab(2, state='normal')
        else:
            # switch selection to selected project
            project_choices.current(INDEX)
            project_choices.configure(state='disabled')
            select_button.configure(state='disabled')
            TABS.tab(1, state='disabled')
            TABS.tab(2, state='disabled')
            start_tracking()

        ACTIVE_PROJECT = get_active()
        update_win()

    def update_win():
        """Update some of the window elements"""
        action_button.configure(text=set_lable())
        info.configure(foreground=get_color())
        if ACTIVE_PROJECT:
            info_label.configure(text='Status:')
            info.configure(text=STATE[ACTIVE_PROJECT.status])

    select_button = ttk.Button(tab, text='Select', command=select_command)
    select_button.grid(column=0, row=3, pady=5)
    select_button.configure(state='enabled') if PROJECTS else select_button.configure(state='disabled')

    if ACTIVE_PROJECT:
        select_button.configure(state='disabled')

    action_button = ttk.Button(tab, text=button_label, command=start_stop_command)
    action_button.grid(column=1, row=3, pady=5)
    action_button.configure(state='enabled') if ACTIVE_PROJECT else action_button.configure(state='disabled')

    update_win()


def setup_tab2(tab):
    # new frame
    new_frame = ttk.LabelFrame(tab, text='New Project Name')
    new_frame.grid(columnspan=2, row=0, padx=5, pady=5, sticky='ew')

    # New Project
    name = tk.StringVar
    name_entered = ttk.Entry(new_frame, width=19, textvariable=name)
    name_entered.grid(column=0, row=0, padx=6, pady=5)
    name_entered.focus()

    # spacer
    spacer_label = ttk.Label(new_frame, text='')
    spacer_label.grid(columnspan=2, row=1, padx=5, pady=5)

    # add button and commands
    def add_command():
        add_project(name_entered.get())
        spacer_label.configure(text='Project was added!', foreground='green')
        name_entered.delete(0, "end")
        setup_tab1(TAB_1)
        TAB_1.update()

    add_button = ttk.Button(tab, text='Add New Project', command=add_command)
    add_button.grid(columnspan=2, row=3, pady=5)


def setup_tab3(tab):
    # remove frame
    remove_frame = ttk.LabelFrame(tab, text='Remove Project')
    remove_frame.grid(columnspan=2, row=0, padx=5, pady=5, sticky='ew')

    # Remove Project
    project_to_axe = tk.StringVar()

    walking_dead = ttk.Combobox(remove_frame, width=18, textvariable=project_to_axe, state='readonly')
    walking_dead['values'] = PROJECT_NAMES
    walking_dead.grid(columnspan=2, row=0, padx=5, pady=5)
    walking_dead.current(INDEX)
    walking_dead.configure(state='enabled') if PROJECTS else walking_dead.configure(state='disabled')

    # spacer
    spacer_label = ttk.Label(remove_frame, text='')
    spacer_label.grid(columnspan=2, row=1, padx=5, pady=5)

    # add button and commands
    def remove_command():
        choice = PROJECTS[PROJECT_NAMES.index(walking_dead.get())].id
        remove_project(choice, safe=False)
        spacer_label.configure(text='Project was removed!', foreground='green')
        walking_dead.set('')
        init_globals()
        setup_tab1(TAB_1)
        if not PROJECTS:
            walking_dead.configure(state='disabled')
            remove_button.configure(state='disabled')

    remove_button = ttk.Button(tab, text='Remove Project', command=remove_command)
    remove_button.grid(columnspan=2, row=3, pady=5)
    remove_button.configure(state='enabled') if PROJECTS else remove_button.configure(state='disabled')


def setup_tab4(tab):
    # about frame
    about_app = 'Python Time Tracker (pytt)\nVer: {}\n\n{}'.format(__version__, __author__)
    about_frame = ttk.LabelFrame(tab, text='About')
    about_frame.grid(columnspan=2, row=0, padx=5, pady=5, sticky='ew')
    about = ttk.Label(about_frame, text=about_app, justify='center')
    about.grid(columnspan=2, row=1, padx=5, pady=5)
    # about.grid(columnspan=2, rowspan=3, padx=5, pady=5)

def get_color():
    """Select the proper color to display"""
    return 'red' if ACTIVE_PROJECT else 'blue'


def set_lable():
    """Set the proper label for the action button"""
    return 'Stop' if ACTIVE_PROJECT else 'Start'


if __name__ == '__main__':
    main()
