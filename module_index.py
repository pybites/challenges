from collections import defaultdict, Counter
import glob
import os
import re

from stdlib import is_std_lib

index = defaultdict(set)

import_regex = re.compile('^(?:from|import)\s(?P<module>\w+).*')

dirname = os.getcwd()


def get_dirs():
    for path in glob.glob('{}/[0-9]*'.format(dirname)):
        yield path


def get_files(path):
    for fi in os.listdir(path):
        if fi.endswith('.py'):
            yield os.path.join(path, fi)


def get_lines(src):
    with open(scr) as f:
        for line in f:
            yield line


if __name__ == '__main__':
    for path in get_dirs():
        day = os.path.basename(path)
        for scr in get_files(path):
            for line in get_lines(scr):
                m = import_regex.match(line)
                if m:
                    mod = m.groupdict()['module']
                    index[mod].add(day)

    cnt = Counter()

    for mod, scripts in sorted(index.items()):
        if mod == 'common' or \
            any(glob.glob(os.path.join(dirname, day, mod + '.py'))
                for day in scripts):
            source = 'own'
        else:
            source = 'stdlib' if is_std_lib(mod) else 'pypi'
        cnt[source] += 1
        appeared_in = ', '.join(sorted(scripts))
        print(f'{mod:<12} | {source:<6} | {appeared_in}')

    total = sum(cnt.values())
    print()
    for source, count in cnt.most_common():
        print(f'{source:<10}: {count:>3} ({count/total*100:.1f}%)')
    print('-' * 30)
    print(f'Total: {total}')
