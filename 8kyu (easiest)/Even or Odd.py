'''Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.'''

def even_or_odd(number):
    
    if number%2 == 0:
        return ("Even")
    else:
        return ("Odd")
    
    pass

'''
TEST CASE:
import codewars_test as test
from solution import even_or_odd
from random import randint, shuffle

@test.describe("Submission tests")
def submission_tests():
    
    def do_test(num, expected):
        test.assert_equals(even_or_odd(num), expected, f'even_or_odd({num}) returned incorrect answer')
    
    @test.it('Positive odd numbers')
    def test_positive_odd():
        do_test(1, "Odd")
        do_test(7, "Odd")
        
    @test.it('Positive even numbers')
    def test_positive_even():
        do_test( 2, "Even")
        do_test(42, "Even")

    @test.it('Negative odd numbers')
    def test_negative_odd():
        do_test(-1, "Odd")
        do_test(-7, "Odd")
            
    @test.it('Negative even numbers')
    def test_negative_even():
        do_test( -2, "Even")
        do_test(-42, "Even")

    @test.it('Zero')
    def test_zero():
        do_test(0, "Even")
        
    @test.it("Random Tests")
    def random_tests():
        def randbase():
            return randint(1, 500)
        
        test_cases = []
        for _ in range(25):
            test_cases += [
                (randbase() *  2,     "Even"), # even positive numbers
                (randbase() * -2,     "Even"), # even negative numbers
                (randbase() *  2 + 1, "Odd" ), # odd positive numbers
                (randbase() * -2 - 1, "Odd" )  # odd negative numbers
            ]
        shuffle(test_cases)
        for num, expected in test_cases:
            do_test(num, expected)'''