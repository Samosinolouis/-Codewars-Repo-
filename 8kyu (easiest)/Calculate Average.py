'''Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.'''

def find_average(numbers):
    sum = 0
    total_avg = 0
    if numbers == 0:
        return 0
    else:
        for total in numbers:
            sum += total
            total_avg = sum / len(numbers)
    return total_avg

'''
TEST CASE:
import codewars_test as test
from solution import find_average

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_average([1, 2, 3]), 2, "Failed for [1, 2, 3]")
        test.assert_equals(find_average([]), 0, "Failed for []")
        test.assert_approx_equals(find_average([1, 2]), 1.5, margin=1e-3, message="Failed for [1, 2]")

@test.describe('Random Tests')
def random_tests():
    
    import random

    # The reference solution should be placed here, in order to prevent the warrior from abusing your reference solution
    def _reference(lst):
        return sum(lst) / len(lst)
    
    def _generate_random_list():
        return random.sample(range(1, 50), random.randint(1, 15))

    # When running a random test, you need to make sure that the expected value is computed first.
    # If the warrior's solution is run first, it may mutate the input list and thus easily bypass them.
    # Also, take extra care on your own reference solution to not mutate the input :)
    def _do_one_test():
        numbers = _generate_random_list()
        expected = _reference(numbers)
        test.assert_approx_equals(find_average(numbers[:]), expected, margin=1e-3, message=f"Failed for {numbers}")

    # The number of random tests must be enough to test every possible aspects of the input.
    # The rule of thumb is 100 tests, but you have to think carefully according to the requirements of your Kata.
    @test.it('Random Test Cases')
    def random_test_cases():
        for _ in range(100):
            _do_one_test()'''