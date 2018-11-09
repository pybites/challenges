#/usr/bin/env python3

from pymediainfo import MediaInfo
from pathlib import Path
import json
import sys

AUDIO_EXTENSIONS = [
    "m4a",
    "mp3",
    "wav",
    "aac",
    "flac",
    "ogg",
    "wma",
    "webm",
    "mpc",
    "dss",
    "ape",
    "aiff"
]

path = Path(str(sys.argv[1]))
if not path.is_dir():
    print("You can only use this script with folders")
    raise SystemExit(1)

total = 0
for ext in AUDIO_EXTENSIONS:
    songs = [
        json.loads(MediaInfo.parse(str(song)).to_json())
        for song in path.glob("*.{}".format(ext))
        ]
    duration = sum(song["tracks"][0]["duration"] for song in songs)
    total += duration

print("Total duration: {}s".format(total // 1000 ))
