import click
import datetime
import pathlib
from tinytag import TinyTag, tinytag


@click.command()
@click.argument('path')
def cli(path):
    """A very simple audio file parser.

    From a given directory output mp3, mp4 and m4a files with length of each
    track and total time for entire directory.

    requires a full path, or relative path from within directory.
    """
    checker = Metadata(path)
    checker.printer()


class Metadata:
    """Class for handling the parsing of directory and utility methods."""

    def __init__(self, path):
        self.path = path

    def parse_directory(self):
        """Parse directory looking for matching file extensions.

        :return list of files
        """
        files = []
        for x in pathlib.Path(self.path).glob('*.m*'):
            if x.is_file():
                x = str(x)  # tinytag needs str, not PosixPath
                files.append(x)
        return files

    def meta(self):
        """Extracts suitable files for extraction of metadata via tinytag

        :return list of audio files and their metadata
        """
        metadata = []
        for x in self.parse_directory():
            audio = TinyTag.get(x)
            metadata.append(audio)
        return metadata

    @classmethod
    def time_in_minutes(cls, duration):
        """Given a time in seconds output H:M:S"""
        if isinstance(duration, list):
            duration = sum(duration)
        time = datetime.datetime.fromtimestamp(duration).strftime("%H:%M:%S")
        return time

    def title(self, data):
        """Take in path of file and split for extracting title.

        :return list of titles
        """
        titles = []
        if isinstance(data, list):
            for title in data:
                segments = title.split('/')[-1]
                titles.append(segments)
            return titles

    def printer(self):
        """Prints metadata to terminal. Checks the file type to ensure
        consistency of output.
        """
        total = []
        files = self.meta()
        titles = self.title(self.parse_directory())
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

            elif isinstance(files[0], tinytag.MP4):  # mp4, m4a
                print("{:^20}\n".format('Legend'))
                print('Title -- [Duration]\n')
                for k, v in dictionary.items():
                    print("{title} -- [{duration}]".format(
                        title=k,
                        duration=Metadata.time_in_minutes(v.duration)))
                    total.append(v.duration)

            else:
                print("Error parsing audio metadata. Could not ascertain"
                      " any information from file.")

        except TypeError as e:
            print(f"{e} error was raised.")
        except IndexError as e:
            print(f"{e} raised, likely no files supported audio files found"
                  f" within directory.")
        finally:
            if total:
                print(f"\nTotal Duration: {self.time_in_minutes(total)}")


if __name__ == '__main__':
    cli()
