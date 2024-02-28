import pytest
from temperature_converter import celsius_to_fahrenheit
from temperature_converter import fahrenheit_to_celsius


@pytest.mark.parametrize(
    "temp_c, result_f", [(0, 32), (100, 212), (-40, -40), (37, 98.6)]
)
def test_celsius_to_fahrenheit(temp_c, result_f):
    # Test cases for celsius_to_fahrenheit function
    assert celsius_to_fahrenheit(temp_c) == result_f


@pytest.mark.parametrize(
    "temp_f, result_c", [(32, 0), (212, 100), (-40, -40), (98.6, 37)]
)
def test_fahrenheit_to_celsius(temp_f, result_c):
    # Test cases for fahrenheit_to_celsius function
    assert fahrenheit_to_celsius(temp_f) == result_c
