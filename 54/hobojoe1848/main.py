import pyperclip

"""Keeping this simple, I needed to populate the clipboard_history list with
a dummy entry to allow me to reference the 'last' index in the list in my print clipboard function"""

clipboard_history = ["dummydata"]

def print_clipboard():
    """This function watches the clipboard and if anything NEW is added
       it'll paste it to stdout."""
    if pyperclip.paste() != clipboard_history[-1]:
        clipboard_history.append(pyperclip.paste())
        print(f"""\n{pyperclip.paste()}""")

if __name__ == "__main__":
    while True:
        print_clipboard()

#TODO
#Need to implement error catching of data that isn't standard text.
#Pop some unicode checks in there to allow for better text handling.
#One day when pigs fly and I have spare time again, implement some sort of GUI!
