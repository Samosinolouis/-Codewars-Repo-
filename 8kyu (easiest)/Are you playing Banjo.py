'''Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.'''

def are_you_playing_banjo(name):
    if name[0]== "r" or name[0]== "R":
        return name + " plays banjo" 
    else: 
        return name + " does not play banjo"

'''
TEST CASE:
import codewars_test as test

try:
    from solution import areYouPlayingBanjo as are_you_playing_banjo
except ImportError:
    from solution import are_you_playing_banjo
    
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(are_you_playing_banjo("Adam"), "Adam does not play banjo")
        test.assert_equals(are_you_playing_banjo("Paul"), "Paul does not play banjo")
        test.assert_equals(are_you_playing_banjo("Ringo"), "Ringo plays banjo")
        test.assert_equals(are_you_playing_banjo("bravo"), "bravo does not play banjo")
        test.assert_equals(are_you_playing_banjo("rolf"), "rolf plays banjo")
    
@test.describe("Random Tests")
def random_tests():
    
    from random import choice
    
    sol = lambda s: f"{s} {'plays banjo' if s[0] in 'rR' else 'does not play banjo'}"
    
    lst = ["Adam", "Bob", "chelsea", "daniel", "Ethan", "fanny", "george", "harry", 
               "Ignatious", "Kyle", "Lavender", "michelle", "peter", "Ragu", "Ryle", "Reaven", 
               "royce", "richard", "rubi", "Reanor", "resh", "Samantha", "trishan", "valde"]
    
    for _ in range(100):
                      
        strng = choice(lst)
        @test.it(f"Testing for are_you_playing_banjo({strng})")
        def test_case():
            test.assert_equals(are_you_playing_banjo(strng), sol(strng), "It should work for random inputs too")
'''