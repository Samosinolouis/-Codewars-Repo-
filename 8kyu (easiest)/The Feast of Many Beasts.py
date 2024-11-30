'''All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name. For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.

Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.

Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.'''

def feast(beast, dish):
    beast_fn = beast[0]
    dish_fn = dish[0]
    beast_ln = beast[-1]
    dish_ln = dish[-1]
    return (beast_fn == dish_fn) and (beast_ln == dish_ln)

'''
TEST CASE:
import codewars_test as test
from solution import feast

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(feast("great blue heron", "garlic naan"), True)
        test.assert_equals(feast("chickadee", "chocolate cake"), True)
        test.assert_equals(feast("brown bear", "bear claw"), False)
        test.assert_equals(feast("marmot", "mulberry tart"), True)
        test.assert_equals(feast("porcupine", "pie"), True)
        test.assert_equals(feast("cat", "yogurt"), False)
        test.assert_equals(feast("electric eel", "lasagna"), False)
        test.assert_equals(feast("slow loris", "salsas"), True)
        test.assert_equals(feast("ox", "orange lox"), True)
        test.assert_equals(feast("blue-footed booby", "blueberry"), True)
        
@test.describe("Random Tests")
def random_tests():    
    import random
    import math
    
    def make_string(min, max):
        array = [];
        possible = "abcdefghijklmnopqrstuvwxyz"
        length = math.ceil((random.random() * max) + min)
        if max < min:
            "Maximum argument should be greater than minimum!"
        for i in range(0,length):
            array.append(possible[math.floor(random.random() * len(possible))])
        return "".join(array)

    def authorSolution(a , b):
        return a[0] == b[0] and a[-1] == b[-1]

    for _ in range (100):
        a = make_string(2, 40)
        b = make_string(2, 40)
        if (random.random() < 0.6):
            #b = a[0] + b + a[-1]
            b = b[:-1] + a[1]
        @test.it(f"testing for feast({a}, {b})")
        def test_case():
            test.assert_equals(feast(a , b), authorSolution(a , b));'''