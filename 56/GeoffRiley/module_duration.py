import argparse
from operator import attrgetter
from pathlib import Path
from statistics import mean
from typing import List, NamedTuple

from tinytag import TinyTag

MUSIC_EXTENSIONS = (
    '.mp3', '.oga', '.ogg', '.opus', '.wav', '.flac', '.wma', '.m4b', '.m4a', '.mp4', '.aiff', '.aifc', '.aif', '.afc',
)


class FileTable(NamedTuple):
    file: Path
    duration: float


def locate_music_files(path: Path) -> List[Path]:
    return [f for f in filter(Path.is_file, path.glob('*')) if f.suffix in MUSIC_EXTENSIONS]


def display_results(files: List[FileTable], graph_width: int = 50) -> None:
    print(f'{"File name":-^40} {"Ext":-^5} {"Duration":-^10}')
    times = [f.duration for f in files]
    max_duration = max(times)
    mean_duration = mean(times)
    mean_pos = int(mean_duration / max_duration * graph_width)
    total_duration = 0.0
    for file in sorted(files, key=attrgetter('duration')):
        duration = file.duration
        portion = int(duration / max_duration * graph_width)
        graph = '*' * portion + ' ' * (graph_width - portion)
        graph = graph[:mean_pos] + '|' + graph[mean_pos + 1:]
        total_duration += duration
        m, s = divmod(duration, 60)
        print(f'{file.file.stem:40} {file.file.suffix:5} {m:>3.0f}:{s:0=5.2f} {graph}')
    m, s = divmod(total_duration, 60)
    print(f'{"Total Duration":->46} {m:>3.0f}:{s:0=5.2f}')


def dir_path(path: str) -> Path:
    if Path(path).is_dir():
        return Path(path)
    raise argparse.ArgumentTypeError(f'{path} is not a valid path')


def process_files(files: List[Path]) -> List[FileTable]:
    result = []
    for file in files:
        duration = TinyTag.get(file).duration
        result.append(FileTable(file, duration))
    return result


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('filepath', type=dir_path)
    args = parse.parse_args()

    print(f'Looking at {args.filepath}')
    files = locate_music_files(args.filepath)
    results = process_files(files)
    display_results(results)


if __name__ == '__main__':
    main()
