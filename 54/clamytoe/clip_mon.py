from dataclasses import dataclass
from datetime import datetime
from hashlib import sha256
from time import sleep

from pyperclip import paste  # type: ignore

clip_log: str = "clip.log"


@dataclass
class ClipMonitor:
    last: str = ""

    def __call__(self) -> None:
        try:
            while True:
                if self.check_hash(paste()):
                    self.save_it(paste())
                sleep(5)
        except KeyboardInterrupt:
            print("\nAborted by user.")
            exit()

    def check_hash(self, content: str) -> bool:
        previous: str = sha256(self.last.encode("utf-8")).hexdigest()
        current: str = sha256(content.encode("utf-8")).hexdigest()
        return False if previous == current else True

    def save_it(self, content: str) -> None:
        try:
            with open(clip_log, "a") as log:
                now: datetime = datetime.now()
                log.write(f"{now}\n--\n{content}\n--\n")
                self.last = content
        except Exception as e:
            print(e)
            exit()


if __name__ == "__main__":
    clip_mon = ClipMonitor()
    clip_mon()
