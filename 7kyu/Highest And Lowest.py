'''In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.'''

def high_and_low(numbers):
    int_array = [int(numbers) for numbers in numbers.split()]
    maxnum = int_array[0]
    minnum = int_array[0]
    for num in int_array:
        if num > maxnum:
            maxnum = num
        elif num < minnum:
            minnum = num
    return str(maxnum) + " " + str(minnum)

'''
TEST CASE:
import codewars_test as test
from solution import high_and_low

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Some Test')
    def some_test():
        test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
    @test.it('Sort Test')
    def sort_test():
        test.assert_equals(high_and_low("10 2 -1 -20"), "10 -20");
    @test.it('Plus Minus Test')
    def plus_minus_test():
        test.assert_equals(high_and_low("1 -1"), "1 -1");
    @test.it('Plus Plus Test')
    def plus_plus_test():
        test.assert_equals(high_and_low("1 1"), "1 1");
    @test.it('Minus Minus Test')
    def minus_minus_test():
        test.assert_equals(high_and_low("-1 -1"), "-1 -1");
    @test.it('Plus Minus Zero Test')
    def plus_minus_zero_test():
        test.assert_equals(high_and_low("1 -1 0"), "1 -1");
    @test.it('Plus Plus Zero Test')
    def plus_plus_zero_test():
        test.assert_equals(high_and_low("1 1 0"), "1 0");      
    @test.it('Minus Minus Zero Test')
    def minus_minus_zero_test():  
        test.assert_equals(high_and_low("-1 -1 0"), "0 -1");
    @test.it('Single Test')
    def single_test():
        test.assert_equals(high_and_low("42"), "42 42");

@test.describe("Random tests")
def random_tests():
    
    from random import randint as rnd
    
    for t in range(10):
        numberlist = []
        for i in range(0,15):
            numberlist.append(rnd(-999,999))
        arg = " ".join(str(a) for a in numberlist)
        exp = "%i %i"%(max(numberlist),min(numberlist))
        @test.it(f"high_and_low(\"{arg}\")")
        def test_case():
            test.assert_equals(high_and_low(arg), exp);'''