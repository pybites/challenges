import datetime
import pathlib
from tinytag import TinyTag, tinytag


class Metadata:

    def __init__(self, path):
        self.path = path

    def parse_directory(self):
        files = []
        for x in pathlib.Path(self.path).glob('*.m*'):
            if x.is_file():
                x = str(x)  # tinytag needs str, not PosixPath
                files.append(x)
        return files

    def meta(self):
        metadata = []
        for x in self.parse_directory():
            audio = TinyTag.get(x)
            metadata.append(audio)
        return metadata

    @classmethod
    def time_in_minutes(cls, duration):
        if isinstance(duration, list):
            duration = sum(duration)
        time = datetime.datetime.fromtimestamp(duration).strftime("%H:%M:%S")
        return time

    def get_name(self, data):
        l = []
        if isinstance(data, list):
            for title in data:
                segments = title.split('/')[-1]
                l.append(segments)
            return l

    def printer(self):
        total = []
        files = self.meta()
        titles = self.get_name(self.parse_directory())
        dictionary = dict(zip(titles, files))
        try:
            print("\nPython Audio Metadata Explorer\n")
            if isinstance(files[0], tinytag.ID3):  # mp3
                for data in files:
                    print("{title:<30}{artist}{duration:>30}".format(
                        title=data.title,
                        artist=data.artist,
                        duration=Metadata.time_in_minutes(data.duration)))
                    total.append(data.duration)

                print(f"\nTotal Duration: {self.time_in_minutes(total)}")

            elif isinstance(files[0], tinytag.MP4):  # mp4, m4a
                print("{:^20}\n".format('Legend'))
                print('Title -- [Duration]\n')
                for k, v in dictionary.items():
                    print("{title} -- [{duration}]".format(
                        title=k,
                        duration=Metadata.time_in_minutes(v.duration)))
                    total.append(v.duration)

                print(f"\nTotal Duration: {self.time_in_minutes(total)}")

            else:
                print("Error parsing audio metadata. Could not ascertain"
                      " any information from file.")

        except TypeError as e:
            print(f"{e} raised.")
        except IndexError as e:
            print(f"{e} raised, likely no files supported audio files found"
                  f" within directory.")


meta = Metadata('audio/Kendrick Lamar - DAMN. (2017)')
meta.printer()
