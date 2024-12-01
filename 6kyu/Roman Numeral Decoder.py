'''Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1
Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000'''

def solution(roman : str) -> int:   
    roman_num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    temp = 0
    total = 0
    for char in roman[::-1]:
        val = roman_num[char]
        if val < temp:
            total -= val
        else:
            total += val
        temp = val
    return total

'''import codewars_test as test
from solution import solution
from random import randrange

@test.describe('Tests')
def tests():

    def do_test(roman : str, n : int):
        actual = solution(roman)
        test.assert_equals(actual, n, f'for roman {roman}')

    @test.it('Fixed Tests')
    def fixed_tests():
        do_test('MMMCMXCIX',       3999)
        do_test('MMMDCCCLXXXVIII', 3888)
        do_test('MM',              2000)
        do_test('MDCLXVI',         1666)
        do_test('M' ,              1000)
        do_test('CD',               400)
        do_test('XC',                90)
        do_test('XL',                40)
        do_test('I' ,                 1)

    def to_roman(n : int) -> str:
        roman_numbers = (
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
            ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
            ('V', 5), ('IV', 4), ('I', 1)
        )

        roman = ''
        for (symbol, value) in roman_numbers:
            if n == 0:
                break
            roman += symbol * (n // value)
            n %= value

        return roman

    @test.it('Random Tests')
    def random_tests():
        for _ in range(300):
            n = randrange(1, 4000)
            roman = to_roman(n)
            do_test(roman, n)'''