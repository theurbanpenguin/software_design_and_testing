import unittest
from test_employee_name import TestEmployeeName
from test_employee_salary import TestEmployeeSalary


def test_suite():
    my_suite = unittest.TestSuite()
    my_suite.addTest(unittest.makeSuite(TestEmployeeSalary))
    my_suite.addTest(unittest.makeSuite(TestEmployeeName))
    return my_suite


if __name__ == "__main__":
    suite = test_suite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
