import os
from tinytag import TinyTag
import argparse
import re
import datetime

mp3and4 = re.compile(r'.mp(3|4)$')
m4a = re.compile('m4a')

def user_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", 
                        help="list all the .mp3, .mp4, .m4a files in the directoy dir",
                        type=str)
    args = parser.parse_args()
    return args.dir

def list_audio(dir_path):
    cum = 0
    for f in os.listdir(dir_path):    
        if mp3and4.search(f) is not None or m4a.search(f) is not None:
            tag = TinyTag.get(os.path.join(dir_path, f))
            artist = str(tag.artist)[:20] + '...' if len(str(tag.artist))>20 else str(tag.artist)
            title = ('-'+ str(tag.title)[:17] + '...') if len(str(tag.title))>20 else '-' + str(tag.title)
            print("{0:30}  {1:30}  :{2:.0f}".format(artist, title, tag.duration))
            cum += tag.duration    
    print('-'*76)
    cum = int(cum)
    total = datetime.timedelta(seconds=cum)
    print("Total"," "*57,f":{total}")

def main():
    dir_path = user_input()
    print(dir_path)
    list_audio(dir_path)

if __name__ == "__main__":
    main()