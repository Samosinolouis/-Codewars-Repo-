'''This code does not execute properly. Try to figure out why.'''

def multiply(a, b):
  return a * b

'''import codewars_test as test 
from solution import multiply
from random import randint, uniform

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(multiply(1,1), 1)
        test.assert_equals(multiply(2,1), 2)
        test.assert_equals(multiply(2,2), 4)
        test.assert_equals(multiply(3,5), 15)
        test.assert_equals(multiply(1.5,2.5), 3.75)
        test.assert_equals(multiply(5,0), 0)
        test.assert_equals(multiply(0,5), 0)
        test.assert_equals(multiply(0,0), 0)
        
    @test.it("Random Test Cases")
    def _():
        for _ in range(100):
            decider = randint(0, 3)
            match decider:
                case 0:
                    a, b = randint(0, 10000), randint(0, 10000)
                    test.assert_equals(multiply(a, b), a * b, f'a = {a}, b = {b}')
                case 1: 
                    a, b = uniform(0, 10000), randint(0, 10000)
                    test.assert_equals(multiply(a, b), a * b, f'a = {a}, b = {b}')
                case 2:
                    a, b = randint(0, 10000), uniform(0, 10000)
                    test.assert_equals(multiply(a, b), a * b, f'a = {a}, b = {b}')
                case 3: 
                    a, b = uniform(0, 10000), uniform(0, 10000)
                    test.assert_equals(multiply(a, b), a * b, f'a = {a}, b = {b}')'''