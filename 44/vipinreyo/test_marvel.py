import unittest

from marvel import (convert_csv_to_dict,
                    most_popular_characters,
                    max_and_min_years_new_characters,
                    percentage_female,
                    good_vs_bad)


class TestMarvel(unittest.TestCase):

    def test_convert_csv_to_dict(self):
        data = list(convert_csv_to_dict())
        self.assertEqual(len(data), 16376)

    def test_most_popular_characters(self):
        expected_no_arg_or_arg_5 = ['Spider-Man',
                                    'Captain America',
                                    'Wolverine',
                                    'Iron Man',
                                    'Thor']
        expected_arg_3 = expected_no_arg_or_arg_5[:3]
        self.assertEqual(most_popular_characters(), expected_no_arg_or_arg_5)
        self.assertEqual(most_popular_characters(5), expected_no_arg_or_arg_5)
        self.assertEqual(most_popular_characters(3), expected_arg_3)

    def test_max_and_min_years_new_characters(self):
        max_, min_ = max_and_min_years_new_characters()
        self.assertEqual(int(max_), 1993)
        self.assertEqual(int(min_), 1958)

    def test_percentage_female(self):
        self.assertEqual(percentage_female(), 24.79)

    def test_good_vs_bad(self):
        # test call arg
        with self.assertRaises(ValueError):
            good_vs_bad('')
        with self.assertRaises(ValueError):
            good_vs_bad('wrong_val')

        males = good_vs_bad('MALE')  # case should not matter
        self.assertEqual(males.get('Bad Characters'), 55)
        self.assertEqual(males.get('Good Characters'), 30)
        self.assertEqual(males.get('Neutral Characters'), 15)

        females = good_vs_bad('female')
        self.assertEqual(females.get('Bad Characters'), 31)
        self.assertEqual(females.get('Good Characters'), 49)
        self.assertEqual(females.get('Neutral Characters'), 20)


if __name__ == '__main__':
    unittest.main()
