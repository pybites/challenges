import re
import unittest

from tags import get_tags, get_top_tags
from tags import get_similarities, TOP_NUMBER

TAG_COUNT = re.compile(r'">([^<]+)</a>\s\((\d+)\)<')
TAGS = 'tags.html'


def parse_tags_html():
    with open(TAGS) as f:
        for line in f:
            if '/tag/' not in line:
                continue
            m = TAG_COUNT.search(line.rstrip())
            if m:
                yield m.groups()[0], int(m.groups()[1])


class test_tags(unittest.TestCase):

    def setUp(self):
        self.tags = get_tags()

    def test_get_tags(self):
        self.assertEqual(len(self.tags), 189)
        self.assertEqual(len(set(self.tags)), 100)
        self.assertEqual(self.tags.count('collections'), 4)
        self.assertEqual(self.tags.count('python'), 10)

    def test_get_top_tags(self):
        top_tags = dict(get_top_tags(self.tags)).items()
        self.assertEqual(len(top_tags), TOP_NUMBER)
        pybites_tags = dict(parse_tags_html())
        for tag in top_tags:
            self.assertIn(tag, pybites_tags.items())

    def test_get_similarities(self):
        similar_tags = dict(get_similarities(self.tags)).items()
        self.assertEqual(len(similar_tags), 3)
        self.assertIn(('game', 'games'), similar_tags)
        self.assertIn(('challenge', 'challenges'), similar_tags)
        self.assertIn(('generator', 'generators'), similar_tags)


if __name__ == "__main__":
    unittest.main()
