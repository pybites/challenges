"""
Writes track's name and length into result.csv 
"""

import subprocess
import re
import datetime
import argparse
import csv

from pathlib import Path, PurePath, PurePosixPath

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', type=str, help='Path to dir')
    args = parser.parse_args()

    with open('result.csv', 'w', newline='') as csvfile:
        fieldnames = ['track_name', 'length']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        p = Path(args.dir_path)
        t0 = datetime.timedelta(seconds=0)

        for i in p.glob('*.*'):
            if PurePath(i).suffix == '.mp3' or PurePath(i).suffix == '.m4a':
                i = re.sub(r'[\s]', '\ ', str(i))
                s = grab_data(i)
                t1 = datetime.timedelta(hours=s.hour, minutes=s.minute,
                                        seconds=s.second)
                print(PurePosixPath(i).name, t1.total_seconds())
                writer.writerow({'track_name': PurePosixPath(i).name,
                                'length': t1.total_seconds()})
                t0 += t1
        print('total', str(t0))
        writer.writerow({'track_name': 'total', 'length': str(t0)})

    
def grab_data(path):
    """
    Return audio's length like datetime object 
    """
    meta_data = subprocess.check_output(
        'ffmpeg -i {} -hide_banner; exit 0'.format(path),
        stderr=subprocess.STDOUT,
        shell=True
    )
    str_time = re.findall(r'Duration: [\d\d:.]+', str(meta_data))[0].split(" ")[1]
    d_time = datetime.datetime.strptime(str_time, '%H:%M:%S.%f')
    return d_time

if __name__ == '__main__':
    main()
