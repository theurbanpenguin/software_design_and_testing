import sys
from employees import Manager
import pytest

run_tests = False


@pytest.mark.skipif(not run_tests, reason="Test disabled")
def test_full_name():
    e = Manager("Vera", "Wang", 0, None)
    assert e.get_full_name() == "Vera Wang"
