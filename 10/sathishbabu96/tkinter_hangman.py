import tkinter
from string import ascii_lowercase
from tkinter import Tk, Frame, Label, Entry, Button

from graphics import hang_graphics
from movies import get_movie

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'
MOVIE = get_movie().lower()

_num_guesses = 0
_wrong_guesses = 0
_movie = [PLACEHOLDER if letter in ASCII else letter for letter in MOVIE]
_guessed = set()
_guessed_wrong = set()


def get_previous_record():
    with open('records.txt', 'r') as fp:
        return int(fp.readlines()[-1])


def event_quit():
    window.destroy()


def event_play_again():
    global _num_guesses, _wrong_guesses, _guessed, _guessed_wrong, _movie, MOVIE
    _num_guesses = 0
    _wrong_guesses = 0
    MOVIE = get_movie().lower()
    _movie = [PLACEHOLDER if letter in ASCII else letter for letter in MOVIE]
    _guessed = set()
    _guessed_wrong = set()
    lbl_movie['text'] = f'{" ".join(_movie)}'
    lbl_message['text'] = ''
    lbl_wrongs['text'] = ''
    lbl_hangman['text'] = ''
    btn_guess['state'] = tkinter.NORMAL
    btn_guess['text'] = f'Guess #{_num_guesses + 1}'


_previous_record = get_previous_record()


def event_hangman(event=None):
    global _num_guesses, _wrong_guesses, _guessed, _guessed_wrong, _previous_record
    letter = ent_guess.get()

    if letter not in ASCII:
        lbl_message['text'] = 'Enter a valid letter (a to z) or (A to Z), Try again!'
        return
    elif letter in _guessed or letter in _guessed_wrong:
        lbl_message['text'] = 'Letter already guessed, Try again!'
        return
    else:
        _num_guesses += 1
        btn_guess['text'] = f'Guess #{_num_guesses + 1}'
        if letter in MOVIE:
            _guessed.add(letter)
            for index, c in enumerate(MOVIE):
                if c == letter:
                    _movie[index] = letter
            lbl_movie['text'] = f'{" ".join(_movie)}'
        else:
            _guessed_wrong.add(letter)
            _wrong_guesses = len(_guessed_wrong)

        if PLACEHOLDER not in _movie:
            message = 'Hurray!, you have won!!!.'
            if _num_guesses < _previous_record:
                message += f'Its a new record!!.\nYour previous record was {_previous_record} guesses\n'
                _previous_record = _num_guesses
                with open('records.txt', 'a') as fp:
                    fp.write('\n')
                    fp.write(f'{_num_guesses}')
            message += f'\nYou have correctly guessed the movie "{MOVIE.upper()}" in {_num_guesses} guesses'
            lbl_wrongs['text'] = ''
            lbl_message['text'] = message
            btn_guess['state'] = tkinter.DISABLED
        if _wrong_guesses > 0:
            lbl_hangman['text'] = HANG_GRAPHICS[_wrong_guesses - 1]
        if _wrong_guesses >= ALLOWED_GUESSES:
            lbl_message['text'] = f'Game over!!!.\nYou have used all your guesses!!. The movie is "{MOVIE.upper()}"'
        if _guessed_wrong:
            lbl_wrongs['text'] = f'Wrongly guessed letters: {", ".join(_guessed_wrong)}'
    ent_guess.delete('0')


window = Tk()
window.title('HANGMAN - MOVIE')

window.rowconfigure(0, minsize=350, weight=2)
window.columnconfigure(0, minsize=300, weight=2)

frm_hangman = Frame(master=window, relief=tkinter.SUNKEN, borderwidth=3)
frm_others = Frame(master=window)

frm_others.rowconfigure([0, 1, 2], minsize=50, weight=1)
frm_others.columnconfigure(0, minsize=10, weight=1)

frm_movie = Frame(master=frm_others, relief=tkinter.RAISED, borderwidth=3)
frm_labels = Frame(master=frm_others)
frm_button = Frame(master=frm_others, relief=tkinter.RAISED, borderwidth=3)

lbl_hangman = Label(master=frm_hangman, text='', bg='black', fg='white', justify=tkinter.LEFT)
lbl_movie = Label(master=frm_movie, text=f'{" ".join(_movie)}', width=15)
lbl_wrongs = Label(master=frm_labels, text='', width=70)
lbl_message = Label(master=frm_labels, text='', width=70)
ent_guess = Entry(master=frm_labels)
btn_play_again = Button(master=frm_button, text='Play Again', command=event_play_again, relief=tkinter.RAISED)
btn_quit = Button(master=frm_button, text='Quit', command=event_quit, relief=tkinter.RAISED)
btn_guess = Button(master=frm_button, text=f'Guess #{_num_guesses + 1}', command=event_hangman, relief=tkinter.RAISED)

window.bind('<Return>', event_hangman)

lbl_hangman.pack(expand=1, fill=tkinter.BOTH)

lbl_movie.pack(expand=1, fill=tkinter.BOTH)
lbl_wrongs.grid(row=0, column=0, sticky='nsew')
lbl_message.grid(row=1, column=0, sticky='nsew')
ent_guess.grid(row=2, column=0, sticky='nsew')

btn_guess.pack(expand=1, fill=tkinter.BOTH)
btn_play_again.pack(expand=1, fill=tkinter.BOTH)
btn_quit.pack(expand=1, fill=tkinter.BOTH)

frm_movie.grid(row=0, column=0, sticky='nsew')
frm_labels.grid(row=1, column=0, sticky='nsew')
frm_button.grid(row=2, column=0, sticky='nsew')

frm_hangman.grid(row=0, column=0, sticky='nsew')
frm_others.grid(row=0, column=1, sticky='nsew')

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

window.geometry("+{}+{}".format(positionRight, positionDown))

window.mainloop()
