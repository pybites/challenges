from rich.console import Console
from rich.live import Live
from time import sleep
from datetime import timedelta


console = Console()


class PomodoroTimer:
    def __init__(self, start_timer=25, break_timer=5):
        self._timer = start_timer
        self._break = break_timer
        self._countdown = timedelta(minutes=self._timer)

    def run(self, prompt="TIMER"):
        with Live(auto_refresh=False) as live:
            while self._countdown:
                console.print(f"{prompt}: {self._countdown}", end="\r")
                self._countdown += timedelta(seconds=-1)
                sleep(1)
                live.refresh()

    def restart(self, start_timer, prompt):
        self._countdown = timedelta(minutes=start_timer)
        self.run(prompt)


timer_duration = int(input("Duration: ").strip())
break_duration = int(input("Break Duration: ").strip())
console.print("\nCTRL+C to quit")
while True:
    try:
        timer = PomodoroTimer(start_timer=timer_duration)
        timer.run()
        timer.restart(start_timer=break_duration, prompt="BREAK")
    except KeyboardInterrupt:
        console.print("TIME'S UP")
        break
