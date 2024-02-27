import unittest
from employees import Manager


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.e = Manager("Vera", "Wang", 2000, None)

    def test_full_name(self):
        self.assertEqual(self.e.get_full_name(), "Vera Wang")

    def test_salary_raise(self):
        self.e.set_salary(100)
        self.assertEqual(self.e.get_salary(), 2100)

    def tearDown(self):
        # Clean resources held by self.e
        pass


if __name__ == "__main__":
    unittest.main()
