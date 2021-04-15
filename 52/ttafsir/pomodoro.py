from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from time import sleep
from datetime import timedelta


console = Console()


minutes = 25
countdown_timer = timedelta(minutes=minutes)


console.print(f"\nPOMODORO TIMER: {minutes}:00")
with Live(auto_refresh=False) as live:
    while countdown_timer:
        console.print(str(countdown_timer), end="\r")
        countdown_timer += timedelta(seconds=-1)
        sleep(1)
        live.refresh()
    console.print("TIME IS UP!")
