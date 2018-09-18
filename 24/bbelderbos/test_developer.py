import unittest

from developer import Developer, MAX_POINTS


class TestDeveloper(unittest.TestCase):

    def setUp(self):
        self.dev1 = Developer('tim')
        self.dev2 = Developer('tom')
        self.dev3 = Developer('tina')

    def test_equality(self):
        self.assertEqual(self.dev1, self.dev2)
        self.dev1.change_karma(self.dev2, 5)
        self.dev2.change_karma(self.dev1, 5)
        self.assertEqual(self.dev1, self.dev2)

    def test_gt_lt(self):
        self.dev1.change_karma(self.dev2, 1)
        self.assertGreater(self.dev1, self.dev2)
        self.dev2.change_karma(self.dev1, 2)
        self.assertGreater(self.dev2, self.dev1)
        self.dev3.change_karma(self.dev2, 3)
        self.assertLess(self.dev2, self.dev3)

    def test_typecheck(self):
        with self.assertRaises(ValueError):
            self.dev1.change_karma(self.dev2, 'string')
        with self.assertRaises(ValueError):
            self.dev1.change_karma(self.dev1, 5)

    def test_repr_str(self):
        expected = "Developer('tim')"
        self.assertEqual(repr(self.dev1), expected)
        self.dev1.change_karma(self.dev3, 5)
        expected = 'Developer tim with 5 karma'
        self.assertEqual(str(self.dev1), expected)

    def test_karma_change(self):
        self.dev1.change_karma(self.dev2, 5)
        self.assertEqual(self.dev1.karma, 5)
        self.dev1.change_karma(self.dev2, -3)
        self.assertEqual(self.dev1.karma, 2)
        self.dev1.change_karma(self.dev2, -4)
        self.assertEqual(self.dev1.karma, -2)
        logmsg = "tim's karma changed to -2"
        self.assertEqual(self.dev1.log[-1], logmsg)

    def test_karma_boundaries(self):
        self.dev1.change_karma(self.dev3, MAX_POINTS+1)
        self.assertEqual(self.dev1.karma, 5)
        self.assertIn('generous', self.dev1.log[-2])
        self.dev1.change_karma(self.dev3, -MAX_POINTS-1)
        self.assertEqual(self.dev1.karma, 0)
        self.assertIn('mean', self.dev1.log[-2])

    def test_greatest_fan_and_call(self):
        self.dev1.change_karma(self.dev2, 1)
        self.dev1.change_karma(self.dev3, 4)
        self.dev1.change_karma(self.dev2, 4)
        self.assertEqual(self.dev1.greatest_fan, 'tom')
        self.dev1.change_karma(self.dev3, 2)
        self.assertEqual(self.dev1.greatest_fan, 'tina')
        self.assertEqual(self.dev1.karma, 11)
        report = self.dev1()
        self.assertRegex(report[2], r'^tina\s+6$')
        self.assertRegex(report[3], r'^tom\s+5$')


if __name__ == '__main__':
    unittest.main()
