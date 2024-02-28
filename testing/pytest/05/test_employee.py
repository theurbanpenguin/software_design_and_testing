from employees import Manager
import pytest


@pytest.fixture()
def setup_employee_and_teardown():
    print("Starting Setup")
    e = Manager("Vera", "Wang", 2000, None)
    yield e
    print("Starting Teardown")
    e = None


def test_full_name(setup_employee_and_teardown):
    e = setup_employee_and_teardown
    assert e.get_full_name() == "Vera Wang"


def test_salary_raise(setup_employee_and_teardown):
    e = setup_employee_and_teardown
    e.set_salary(100)
    assert e.get_salary() == 2100
