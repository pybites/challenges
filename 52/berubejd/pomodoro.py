import argparse
import time

def progress_bar(progress: int, length: int = 20, msg_prefix: str = '', msg_complete: str = 'Complete!', complete: int = 100, suppress_nl: bool = False) -> None:
    """Display a progress bar with optional messaging
    
       The only required parameter is 'progress' which should represent a percentage between 0 and 100.
       
       By setting 'complete' to zero it is possible to work as a countdown timer, as well.
       
       Examples:
       
       for i in range(11):
           progress_bar(i*10, 20)
           time.sleep(1)

       for i in range(10, -1, -1):
           progress_bar(progress=i*10, length=20, complete=0, msg_complete='Time is up!')
           time.sleep(1)

        for i in range(11):
           progress_bar(i*10, 20, msg_prefix=f'Timer 3 ({i*10:3}):')
           time.sleep(1)
       
    """
    
    FILL_CHAR = '#'
    BLANK_CHAR = ' '

    if progress < 0 or progress > 100:
        raise ValueError('Progress must be a value between 0 and 100')

    if len(msg_complete) > length:
        raise ValueError('Message must be shorter than progress bar length!')

    if progress != complete:
        progress_length = int(progress / 100 * length)
        fill = '#' * progress_length + BLANK_CHAR * (length - progress_length)
        line_term = ''
    else:
        padding = BLANK_CHAR * int((length - len(msg_complete)) / 2)
        fill = padding + msg_complete + padding

        if len(fill) < length:
            fill = fill + BLANK_CHAR

        if suppress_nl:
            line_term = ''
        else:
            line_term = '\n'

    print(f'\r{msg_prefix} [ {fill} ] {int(progress):3}% ', end=line_term, flush=True)


def test_input(suppress: bool = False) -> None:
    response = input("\aPress ENTER to continue or type 'Quit' to exit... ")

    if response.lower() == 'quit':
        exit()

    if not suppress:
        print()

def timer(seconds: int, prefix: str, suppress: bool) -> None:
    remaining = seconds

    while True:
        progress = remaining / seconds * 100
            
        progress_bar(progress=progress, length=20, complete=0, msg_complete='Time is up!', msg_prefix=prefix + f' ({time.strftime("%M:%S", time.gmtime(remaining))} remaining): ', suppress_nl=suppress)
        time.sleep(1)
            
        remaining -= 1

        if remaining < 0:
            break

def main() -> None:
    # Setup command line argument parsing
    parser = argparse.ArgumentParser()
    parser.version = '1.0'

    parser.add_argument('-n', '--name', action='store', type=str, default='My Pomodoro Task', metavar='text', help="The name to assign to this task")
    parser.add_argument('-p', '--pomodoro', action='store', type=int, default=25, metavar='minutes', help="The length of each pomodoro in minutes")
    parser.add_argument('-c', '--count', action='store', type=int, default=4, metavar='number', help="The number of pomodoros to complete")
    parser.add_argument('-s', '--short-break-duration', action='store', type=int, default=5, metavar='minutes', help="The length of each short break in minutes")
    parser.add_argument('-l', '--long-break-duration', action='store', type=int, default=15, metavar='minutes', help="The length of each long break in minutes")
    parser.add_argument('-v', '--version', action='version', help="Show the version number and exit")
    parser.add_argument('-d', '--debug', action='store_true', help="Sets low timers for testing")

    args = parser.parse_args()

    # Reset timers if debug option was used
    if args.debug:
        args.pomodoro = .5
        args.short_break_duration = .1
        args.long_break_duration = .2

    # Output to user the parameters for the coming Pomodoro Timer
    print()
    print(f'{args.name}')
    print(f'{"-" * len(args.name)}')
    print(f'Starting "{args.name}" with {args.count} pomodoros of {args.pomodoro} minutes each.  There will be a {args.short_break_duration} minute break between each pomodoro and a {args.long_break_duration} minute break after every 4 pomodoros.')
    print()

    test_input()

    # Start the timer process
    for count, interval in enumerate(range(1, args.count + 1), 1):

        # Set up and generate the Pomodoro timer
        duration = args.pomodoro * 60
        prefix = f'Pomodoro {count} '
        suppress = True

        timer(duration, prefix, suppress)

        if not count == args.count:

            if interval % 4 == 0:
                # Time for long break
                test_input()

                duration = args.long_break_duration * 60
                prefix = f'Long Break '
                suppress = True

                timer(duration, prefix, suppress)
            else:
                # Time for short break
                test_input(True)

                duration = args.short_break_duration * 60
                prefix = f'Short Break'
                suppress = True

                timer(duration, prefix, suppress)

            # Alert that it is time for the next pomodoro
            print('\a', end='')

        else:
            print(f'\a\n\nCongratulations!  You have just completed the "{args.name}" pomodoro!\n')

if __name__ == '__main__':
    main()
