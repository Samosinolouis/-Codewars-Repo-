'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''

def add_binary(a,b):
    return bin(a+b)[2:]



'''
TEST CASE
import codewars_test as test
from solution import add_binary

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(add_binary(1,1),"10")
        test.assert_equals(add_binary(0,1),"1")
        test.assert_equals(add_binary(1,0),"1")
        test.assert_equals(add_binary(2,2),"100")
        test.assert_equals(add_binary(51,12),"111111")
        test.assert_equals(add_binary(5,9),"1110")
        test.assert_equals(add_binary(10,10),"10100")
        test.assert_equals(add_binary(100,100),"11001000")
        test.assert_equals(add_binary(4096,1),"1000000000001")
        test.assert_equals(add_binary(0,2174483647),"10000001100110111111110010111111")
        
@test.describe("Random tests")
def _():
    
    from random import randint
    sol_binary=lambda a,b: bin(a+b)[2:]
    
    for _ in range(40):
        top=10**randint(1,32)
        a,b=randint(0,top),randint(0,top)
        @test.it(f"Testing for add_binary({a}, {b})")
        def _():
            test.assert_equals(add_binary(a,b), sol_binary(a,b))'''




