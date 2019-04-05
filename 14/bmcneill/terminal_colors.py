from functools import wraps

def print_text_as_color(color):
    def pass_through(func):
        '''Decorator to print text using terminal colors'''
        @wraps(func)
        def wrapper(*args):
            colors = {"red": "\33[31m",
                      "white":'\33[37m',
                      "violet":'\33[35m'}
            terminal_color = colors.get(color)
            msg = f"{terminal_color}" + func(*args) + "\033[0m"
            print(msg)
        return wrapper
    return pass_through

@print_text_as_color('violet')
def print_text(text='I code with PyBites with colors!'):
    return text

if __name__ == "__main__":
    print_text()