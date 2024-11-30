'''Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5'''

import math

def litres(time):
    return math.floor(time * 0.5)

'''
TEST CASE:
import codewars_test as test
from solution import litres

@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(litres(2), 1, 'should return 1 litre')
        test.assert_equals(litres(1.4), 0, 'should return 0 litres')
        test.assert_equals(litres(12.3), 6, 'should return 6 litres')
        test.assert_equals(litres(0.82), 0, 'should return 0 litres')
        test.assert_equals(litres(11.8), 5, 'should return 5 litres')
        test.assert_equals(litres(1787), 893, 'should return 893 litres')
        test.assert_equals(litres(0), 0, 'should return 0 litres')
    
@test.describe("Random Tests")
def random_tests():
    
    from random import randint
    
    def ans(time):
        return int(time/2)
    
    for _ in range(100):
        time=randint(0,1000)
        @test.it(f"Testing for litres({time})")
        def test_case():
            test.assert_equals(litres(time), ans(time), "It should work for random inputs too")'''