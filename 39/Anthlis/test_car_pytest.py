import pytest
from Car import Car

speed_data = {45, 50, 55, 100}

# With pytest fixtures you can create small test units that can be reused across the testing module.
# All you need is to mark a reusable unit with @pytest.fixture.

# my_car() is a fixture function that creates a Car instance with the speed value equal to 50.
# It is used in test_car_accelerate and test_car_brake to verify correct execution of the
# corresponding functions in the Car class.

# @pytest.fixture
# def my_car():
#     return Car(50)

# def test_car_accelerate(my_car):
#     my_car.accelerate()
#     assert my_car.speed == 55

# def test_car_brake(my_car):
#     my_car.brake()
#     assert my_car.speed == 45

# You might want to run your tests on the predefined set of data.
# PyCharm supports test parametrization implemented in pytest through @pytest.mark.parametrize.

@pytest.mark.parametrize("speed_accelerate", speed_data)
def test_car_accelerate(speed_accelerate):
    car = Car(50)
    car.accelerate()
    assert car.speed == speed_accelerate


@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake








