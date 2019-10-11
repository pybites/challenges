import os
from dataclasses import dataclass, field, astuple
import datetime

import pandas as pd
import eyed3


@dataclass
class Song:
    """Class for tracking song name and length in seconds."""

    path: str
    title: str
    song_length: int = field(init=False)

    def __post_init__(self):
        self.song_length = self.get_song_length()
        self.title = self.title.replace(".mp3", "")

    def get_song_length(self) -> int:
        try:
            song = eyed3.load(os.path.join(self.path, self.title))
            return song.info.time_secs
        except AttributeError as e:
            print(f"Could not get length for {self.title}, {e}. Using 0.")
            return 0
        except Exception as e:
            raise Exception(f"{type(e)} error with {self.title}, {e}")

    def as_tuple(self) -> tuple:
        return astuple(self)


def find_mp3_files(starting_dir=None):
    if starting_dir is None:
        starting_dir = os.curdir

    songs = []

    for directory, _, files in os.walk(starting_dir):
        for filename in files:
            if filename.endswith("mp3"):
                songs.append(Song(directory, filename).as_tuple())

    columns = ["Directory", "Name", "Length"]

    df = pd.DataFrame(songs, columns=columns)

    total = pd.DataFrame([["", "Total", df.Length.sum()]], columns=columns)

    df = df.append(total)

    df["Length"] = df["Length"].map(
        lambda length: str(datetime.timedelta(seconds=length))
    )

    return df


if __name__ == "__main__":
    files = find_mp3_files("/Users/dshorstein/Music/Logic/TBD Songs/")
    print(files)
