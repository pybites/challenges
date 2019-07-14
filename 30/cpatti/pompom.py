import json
import argparse
import fire
import time
import sys
import readchar
from logbook import RotatingFileHandler, info, notice, debug, StreamHandler
from pathlib import Path
from datetime import datetime, timedelta

def back_to_work():
    info("Back to work!")
    print('\a')
    print('\a')


def decide_break_time(completed_poms, mini_break_time, long_break_time):
    """Determine whether or not the user has earned a break, and if so, how long?"""
    break_reward_pom_count = 4
    if (completed_poms / break_reward_pom_count) == 0:
        return(long_break_time)
    else:
        return(mini_break_time)


def start(mini_break_time, long_break_time):
    config_path = Path.home() / ".config/pompom"
    config_path.mkdir(parents=True, exist_ok=True)
    poms_file = config_path / "Pomodoro.json"
    debug(f"config_path: {config_path} poms_file: {poms_file}")
    Pomodoros = []
    # A single Pomodoro is 25 minutes long.
    pomodoro_seconds = 60 * 25
    completed_poms = 0

    try:
        with open(poms_file,'r') as pfile:
            Pomodoros = json.load(pfile)
    except OSError:
        info("No previously stored Pomodoros! Welcome!")

    Pom={}
    try:
        info("Pomodoro timer starting! Hit any key when done. Hit 'Ctrl-c' to log an interrupt.")
        while True:
            start_time = datetime.now()
            Pom['start_time'] = str(start_time)
            info(f"Starting next Pomodoro at: {start_time}")
            time.sleep(pomodoro_seconds)
            completed_poms = completed_poms + 1
            info(f"{completed_poms} pomodoros complete!")
            print('\a')

            break_time = decide_break_time(completed_poms, mini_break_time, long_break_time)
            info(f"Well done! Take a {break_time} minute break!")
            time.sleep(break_time)
            back_to_work()

    except KeyboardInterrupt:
        end_time = datetime.now()

        elapsed = end_time - start_time
        pom_seconds = elapsed.seconds

        info("Ending session. Hit 'i' if this was an interrupt. Anything else to count this pom.")
        interrupt_prompt = readchar.readchar()
        if interrupt_prompt.lower() is not 'i':
            finished_one_pom = start_time + timedelta(minutes=25)
            if datetime.now() > finished_one_pom:
                completed_poms = completed_poms + 1

        info(f"Pom seconds: {pom_seconds} Finished poms: {completed_poms}")

        Pom['end_time'] = str(end_time)
        Pom['elapsed'] = str(elapsed)
        Pom['completed'] = completed_poms

        Pomodoros.append(Pom)
        with open(poms_file,'w') as pfile:
            json.dump(Pomodoros, pfile)



if __name__ == '__main__':
    RotatingFileHandler("Pompom.log").push_application()
    StreamHandler(sys.stderr, level='INFO', bubble=True).push_application()

    fire.Fire(start)
