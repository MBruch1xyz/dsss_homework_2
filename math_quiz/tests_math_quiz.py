import unittest
from math_quiz import random_integer, random_operator, math_operation

class TestMathQuizFunctions(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if the random operator is one of the expected operators
        operators = set(['+', '-', '*'])
        for _ in range(1000):  # Test a large number of random values
            rand_op = random_operator()
            self.assertIn(rand_op, operators)

    def test_math_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '*', '10 * 3', 30),
            (8, 4, '-', '8 - 4', 4),  # Additional test case
            (7, 2, '*', '7 * 2', 14),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                result = math_operation(num1, num2, operator)
                # Verify the generated problem and answer match the expected values
                self.assertEqual(result[0], expected_problem)
                self.assertEqual(result[1], expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
