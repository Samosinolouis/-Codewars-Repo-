'''You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

Example(Input1, Input2 --> Output):

6, 10 --> 32
3, 3 --> 9
Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.'''

def area_or_perimeter(l , w):
    if l==w :
        return l*w
    else :
        return (l+w)*2

'''
TEST CASE:
import codewars_test as test
from solution import area_or_perimeter

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(area_or_perimeter(4, 4), 16)
        test.assert_equals(area_or_perimeter(6, 10), 32)

@test.describe("Random Tests")
def random_tests():  
    import random
            
    def solution(l, w):
        return l * l if l == w else (l + w) * 2
    
    for i in range(100):
        a, b = (i * 1200) + 2, (i * 2100) + 2
        @test.it(f"testing for area_or_perimeter({a}, {b})")
        def test_case():
            test.assert_equals(area_or_perimeter(a, b), solution(a, b))
        
    for i in range(100):
        a, b = (i * 100) + 20, (i * 100) + 20
        @test.it(f"testing for area_or_perimeter({a}, {b})")
        def test_case():
            test.assert_equals(area_or_perimeter(a, b), solution(a, b))
    
    for i in range(100):
        a, b = random.randint(100, 1200), random.randint(100, 1500)
        @test.it(f"testing for area_or_perimeter({a}, {b})")
        def test_case():
            test.assert_equals(area_or_perimeter(a, b), solution(a, b))'''