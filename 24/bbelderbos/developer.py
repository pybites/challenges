from collections import Counter
from functools import total_ordering

ROW_FMT = '{:<20} {:>5}'
MAX_POINTS = 5


@total_ordering
class Developer:

    def __init__(self, name):
        self.name = name
        self.scores = Counter()
        self.log = []

    @property
    def karma(self):
        return sum(self.scores.values())

    @property
    def greatest_fan(self):
        return self.scores.most_common(1)[0][0]

    def __call__(self):
        out = [ROW_FMT.format('NAME', 'SCORE')]
        out.append('-'*26)
        for name, score in self.scores.most_common():
            out.append(ROW_FMT.format(name, score))
        return out

    def __repr__(self):
        return 'Developer({!r})'.format(self.name)

    def __str__(self):
        return 'Developer {} with {} karma'.format(self.name, self.karma)

    def change_karma(self, giver, points):
        if not isinstance(points, int):
            raise ValueError('please use int for points')

        if giver.name == self.name:
            raise ValueError('cannot give karma to self')

        if abs(points) > MAX_POINTS:
            mood = 'generous' if points > 0 else 'mean'
            msg = 'Little too {} no? '.format(mood)
            msg += 'Using max {} points'.format(MAX_POINTS)
            self.log.append(msg)
            points = MAX_POINTS if points > 0 else -MAX_POINTS

        self.scores[giver.name] += points
        poses = "'" if self.name.endswith('s') else "'s"

        self.log.append('{}{} karma changed to {}'.format(self.name,
                                                          poses,
                                                          self.karma))

    def __eq__(self, other):
        return self.karma == other.karma

    def __lt__(self, other):
        return self.karma < other.karma
