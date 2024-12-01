'''Is the string uppercase?
Task
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.'''

def is_uppercase(inp):
    upper = ''.join(char.upper() for char in inp)
    if inp != upper:
        return False
    else:
        return True

'''import codewars_test as test
from solution import is_uppercase

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        def gen_test_case(inp, res):
            test.assert_equals(is_uppercase(inp), res, inp)
        gen_test_case("c", False)
        gen_test_case("C", True)
        gen_test_case("hello I AM DONALD", False)
        gen_test_case("HELLO I AM DONALD", True)
        gen_test_case("$%&", True)

@test.describe("Random Tests")
def random_tests():
    from string import ascii_lowercase, ascii_uppercase
    from random import sample, randrange

    CHARS = (ascii_lowercase
             + ascii_uppercase
             + ' _!@#$%^&*())_+1234567890~`{}|[]\:";<>?,./')

    for i in range(50):
        strng = "".join(sample(CHARS, randrange(1, 51)))
        if i % 5 == 0:
            strng = strng.upper()
        expected = strng == strng.upper()
        @test.it(f'Testing for {repr(strng)}')
        def _():
            test.assert_equals(is_uppercase(strng), expected, strng)'''