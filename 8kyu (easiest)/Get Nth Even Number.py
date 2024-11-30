'''Return the Nth Even Number

Example(Input --> Output)

1 --> 0 (the first even number is 0)
3 --> 4 (the 3rd even number is 4 (0, 2, 4))
100 --> 198
1298734 --> 2597466
The input will not be 0.'''

def nth_even(n):
    return (n-1)*2;

'''
Test Case:
import codewars_test as test
from solution import nth_even

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(nth_even(1), 0)
        test.assert_equals(nth_even(2), 2)
        test.assert_equals(nth_even(3), 4)
        test.assert_equals(nth_even(100), 198)
        test.assert_equals(nth_even(1298734), 2597466)

@test.describe("Random Tests")
def random_tests():
    
    from random import randint
    
    sol=lambda n: n*2-2
    
    for _ in range(100):
        n=randint(1,1000000000)
        @test.it(f"Testing for nth_even({n})")
        def test_case():
            test.assert_equals(nth_even(n),sol(n))'''