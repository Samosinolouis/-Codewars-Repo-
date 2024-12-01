'''Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321'''

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

'''
TEST CASE:
import codewars_test as test

try:
    from solution import Descending_Order as descending_order
except ImportError:
    from solution import descending_order

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(descending_order(0), 0)
        test.assert_equals(descending_order(1), 1)
        test.assert_equals(descending_order(111), 111)
        test.assert_equals(descending_order(15), 51)
        test.assert_equals(descending_order(1021), 2110)
        test.assert_equals(descending_order(123456789), 987654321)

@test.describe("Random tests")
def random_tests():
    from random import randint
    
    for _ in range(50):
        n = randint(0, 10**randint(1,10))
        expected = int("".join(sorted(str(n), reverse=True)))
        @test.it(f"testing for descending_order({n})")
        def test_case():
            test.assert_equals(descending_order(n),expected)'''