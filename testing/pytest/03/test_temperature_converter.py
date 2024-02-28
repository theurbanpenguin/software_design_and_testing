from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    # Test cases for celsius_to_fahrenheit function
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == 98.6


def test_fahrenheit_to_celsius():
    # Test cases for fahrenheit_to_celsius function
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(98.6) == 37
