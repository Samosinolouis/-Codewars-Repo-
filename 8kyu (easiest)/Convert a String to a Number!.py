'''We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7'''

def string_to_number(s):
    return int(s)


'''
TEST CASE:
import codewars_test as test
from solution import string_to_number
from random import randint

@test.describe("string_to_number")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_to_number("1234"), 1234)
        test.assert_equals(string_to_number("605"), 605)
        test.assert_equals(string_to_number("1405"), 1405)
        test.assert_equals(string_to_number("-7"), -7)

@test.describe("Random Tests")
def random_tests():
    for _ in range(100):
        num = randint(-50000, 50000)
        @test.it(f"Testing for string_to_number('{num}')")
        def test_case():
            test.assert_equals(string_to_number(str(num)), num, "It should work for random inputs too")'''