'''Unfinished Loop - Bug Fixing #1
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!'''

def create_array(n):
    res=[]
    i=1
    while i<=n: 
      res +=[i]
      i = i+1
    return res

'''
TEST CASE:
import codewars_test as test
from solution import create_array

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(create_array(1),[1])
        test.assert_equals(create_array(2),[1,2])
        test.assert_equals(create_array(3),[1,2,3])
        test.assert_equals(create_array(4),[1,2,3,4])
        test.assert_equals(create_array(5),[1,2,3,4,5])
        test.assert_equals(create_array(6),[1,2,3,4,5,6])
        test.assert_equals(create_array(7),[1,2,3,4,5,6,7])
        test.assert_equals(create_array(8),[1,2,3,4,5,6,7,8])
        test.assert_equals(create_array(9),[1,2,3,4,5,6,7,8,9])
        test.assert_equals(create_array(10),[1,2,3,4,5,6,7,8,9,10])

@test.describe("Random Tests")
def random_tests():
    
    from random import randint
    
    create_sol=lambda n: [*range(1,n+1)]

    for _ in range(40):
        n=randint(11,200)
        @test.it(f"Testing for create_array({n})")
        def test_case():
            test.assert_equals(create_array(n),create_sol(n))'''