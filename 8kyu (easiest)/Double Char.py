'''Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!'''

def double_char(s):
    new_string = ''
    for char in s:
        new_string += char * 2
    return new_string

'''import codewars_test as test
from solution import double_char

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(double_char("String"),"SSttrriinngg")
        test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
        test.assert_equals(double_char("1234!_ "),"11223344!!__  ")
        
@test.describe("Random Tests")
def random_tests():    
    from random import shuffle
    import random
    import string

    def ref(s):
        return ''.join(c*2 for c in s)

    def random_string():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,200)))

    for l in range(200):
        s = random_string()
        @test.it(f's = {repr(s)}')
        def basic_test_cases():
            test.assert_equals(double_char(s), ref(s))'''