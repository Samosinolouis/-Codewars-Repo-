'''You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"'''

def get_middle(s):
    middle = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[middle]
    else:
        return s[middle-1:middle+1]

'''import codewars_test as test
from solution import get_middle

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(get_middle("test"),"es")
        test.assert_equals(get_middle("testing"),"t")
        test.assert_equals(get_middle("middle"),"dd")
        test.assert_equals(get_middle("A"),"A")
        test.assert_equals(get_middle("of"),"of")'''