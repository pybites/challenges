#!/usr/bin/env python3.7


import glob
import os
import sys
import pathlib

import pandas as pd
from tabulate import tabulate
from tinytag import TinyTag, TinyTagException


media_path = sys.argv[1]

# this glob pattern can lead to some false matches, but good enough for now
pattern = '*.[Mm][4Pp][34Aa]'

df = pd.DataFrame(columns=['FILE', 'DURATION'])

for file in glob.iglob(os.path.join(media_path, '**', pattern), recursive=True):

    try:
        tag = TinyTag.get(file)
        df = df.append({'FILE': pathlib.Path(file).name, 'DURATION': round(tag.duration)}, ignore_index=True)
    except TinyTagException:
        pass

if not df.empty:

    # convert DURATION from float64 to timedelta64
    df['DURATION'] = pd.to_timedelta(df['DURATION'], unit='s')

    # dig out the "time parts" for "easier" formatting
    comp_min = df['DURATION'].min().components
    comp_max = df['DURATION'].max().components
    comp_mean = df['DURATION'].mean().components
    comp_std = df['DURATION'].std().components
    comp_sum = df['DURATION'].sum().components

    report = "\n" \
             f"PATH: {media_path}\n" \
             f"FILES: {df.shape[0]}\n\n" \
             f"{tabulate(df, headers='keys', showindex=False, tablefmt='github')}\n\n\n" \
             f"{'=' * 21}\n" \
             f"STAT  : DAYS HH:MM:SS\n" \
             f"{'=' * 21}\n" \
             f"MIN   : {'%4s %02d:%02d:%02d' % (comp_min.days, comp_min.hours, comp_min.minutes, comp_min.seconds)}\n" \
             f"MAX   : {'%4s %02d:%02d:%02d' % (comp_max.days, comp_max.hours, comp_max.minutes, comp_max.seconds)}\n" \
             f"MEAN  : {'%4s %02d:%02d:%02d' % (comp_mean.days, comp_mean.hours, comp_mean.minutes, comp_mean.seconds)}\n" \
             f"STD   : {'%4s %02d:%02d:%02d' % (comp_std.days, comp_std.hours, comp_std.minutes, comp_std.seconds)}\n" \
             f"TOTAL : {'%4s %02d:%02d:%02d' % (comp_sum.days, comp_sum.hours, comp_sum.minutes, comp_sum.seconds)}\n" \
             f"{'-' * 21}\n"

    print(report)
