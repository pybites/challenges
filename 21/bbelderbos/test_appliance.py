import pytest

# examples from:
# https://energy.gov/energysaver/estimating-appliance-and-home-electronic-energy-use

# TODO: write more test cases

from appliance import ApplianceCost

def test_appliance():
    k = ApplianceCost('kettle', 1500, 'spain', 0.11)
    use = 365 * 60
    k.consume(use)
    assert k.cost == 60.23

    s = ApplianceCost('shredder', 360, 'france', 0.11)
    use = 52 * 15
    s.consume(use)
    assert s.cost == 0.51

if __name__ == '__main__':
    pytest.main()
