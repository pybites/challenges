#!/usr/bin/env python3.8


def progress_bar(
    progress: int,
    length: int = 20,
    msg_prefix: str = "",
    msg_complete: str = "Complete!",
    complete: int = 100,
    suppress_nl: bool = False,
) -> None:
    """Display a progress bar with optional messaging
       The only required parameter is 'progress' which should represent a percentage expressed as am integer between 0 and 100.
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

    FILL_CHAR = "#"
    BLANK_CHAR = " "

    if progress < 0 or progress > 100:
        raise ValueError("Progress must be a value between 0 and 100")

    if len(msg_complete) > length:
        raise ValueError("Message must be shorter than progress bar length!")

    if progress != complete:
        progress_length = int(progress / 100 * length)
        fill = "#" * progress_length
        line_term = ""
    else:
        fill = msg_complete
        length = f"^{length}"

        line_term = "" if suppress_nl else "\n"

    print(
        f"\r{msg_prefix} [ {fill:{length}} ] {int(progress):3}% ",
        end=line_term,
        flush=True,
    )


if __name__ == "__main__":
    progress_bar(progress=40, length=20, complete=100, msg_complete="Time is up!")
