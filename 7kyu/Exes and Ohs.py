'''Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false'''

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


'''import codewars_test as test
from solution import xo

@test.describe("Fixed tests")
def _():
    test_cases = [
        ("xo",      True, None),
        ("XO",      True, None),
        ("xo0",     True, "Zero is not an O"),
        ("xxxoo",   False, None),
        ("ooxx",    True, None),
        ("xooxx",   False, None),
        ("ooxXm",   True, "Comparison is case-insensitive"),
        ("zpzpzpp", True, "when no 'x' and 'o' is present should return true"),
        ("zzoo",    False, None),
        ("oxOx",    True, None),
        ("",        True, "Empty string contains equal amount of x and o"),
        ("xxxxxoooxooo", True, None),
        ("xxxxxoooXooo", True, "Comparison is case-insensitive"),
        ("abcdefghijklmnopqrstuvwxyz", True, "Alphabet contains equal amount of x and o")
    ]
    for s, expected, msg in test_cases:
        @test.it(f"{s = }")
        def _():
            test.assert_equals(xo(s), expected, msg)

@test.describe("Random tests")
def _():
    from random import randint, shuffle, choice
    for _ in range(0, 50):
        s, length, c = [], randint(0,30), 0
        for i in range(length):
            match randint(0,2):
                case 0: s.append(choice("xX")); c += 1
                case 1: s.append(choice("oO")); c -= 1
                case 2: s.append(choice("abcdefghijklmnpqrstuvwyzABCDEFGHIJKLMNPQRSTUVWYZ0123456789"))
        if randint(0,2) == 0: s += ["xo"[c>0]]*abs(c); c = 0
        s = "".join(s)
        @test.it(f"{s = }")
        def t():
            exp = c == 0
            test.assert_equals(xo(s), exp)'''