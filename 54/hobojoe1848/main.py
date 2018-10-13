import pyperclip
import sys
import time

clipboard_history = ["foo"]

def print_clipboard():
    if pyperclip.paste() != clipboard_history[-1]:
        clipboard_history.append(pyperclip.paste())
        print(f"""\n{pyperclip.paste()}""")

if __name__ == "__main__":
    while True:
        print_clipboard()
