import populationgrowth

# see if the dict has more than 0 items - should indicate that loading was successful, right?
def test_get_population_by_country():
    assert len(populationgrowth.get_population_by_country()) > 0


# see if the calculation for getting absolute growth is correct
def test_get_absolute_growth():
    assert populationgrowth.get_absolute_growth(20, 10) == 10


# see if calculation for getting relative growth is correct
def test_get_relative_growth():
    assert populationgrowth.get_relative_growth(20, 10) == 100.0
    assert populationgrowth.get_relative_growth(10, 20) == -50.0
    assert populationgrowth.get_relative_growth(10, 10) == 0.0


# see if things are properly printed using capfd
def test_print_results(capfd):
    countries = dict()
    countries['test_country'] = populationgrowth.Country(population_1950=10, population_2015=10,
                                                         absolute_growth=populationgrowth.get_absolute_growth(10, 10),
                                                         relative_growth=populationgrowth.get_relative_growth(10, 10))
    populationgrowth.print_results(countries)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1. test_country: 1950:10, 2015:10, 0, 0.0%'
