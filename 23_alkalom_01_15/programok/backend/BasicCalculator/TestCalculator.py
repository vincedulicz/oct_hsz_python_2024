import unittest
from o_23_alkalom_01_15.backend.BasicCalculator.Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("\nsetup before testing...\n")
        self.calculation = Calculator(8, 2)

    def tearDown(self):
        print("\nteardwon after testing...\n")

    def test_sum(self):
        print("run test_sum...")
        self.assertEqual(self.calculation.get_sum(), 10, "The sum is wrong")

    def test_diff(self):
        print("run test_diff...")
        self.assertEqual(self.calculation.get_difference(), 6, "the diff is wrong")

    def test_product(self):
        print("run test_prod...")
        self.assertEqual(self.calculation.get_product(), 16, "the prod is wrong")

    def test_quotient(self):
        print("run test_quo...")
        self.assertEqual(self.calculation.get_quotient(), 4, "the quo is wrong")


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestCalculator('test_sum'))
    suite.addTest(TestCalculator('test_diff'))
    suite.addTest(TestCalculator('test_product'))
    suite.addTest(TestCalculator('test_quotient'))

    return suite

if __name__ == '__main__':
    # 0 quite -> total num
    # 1 default -> . sikeres ; F sikertelen
    # 2 verbose -> help string

    # class
    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    )

    # suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())