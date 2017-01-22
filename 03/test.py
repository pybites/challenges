import re

TAG_COUNT = re.compile(r'">([^<]+)</a>\s\((\d+)\)<')
TAGS = 'tags.html'


def _read_html():
    with open(TAGS) as f:
        return f.readlines()


def parse_tags_html():
    for line in _read_html():
        if '/tag/' not in line:
            continue
        m = TAG_COUNT.search(line.rstrip())
        if m:
            yield m.groups()[0], int(m.groups()[1])


if __name__ == "__main__":
    parse_tags_html()
