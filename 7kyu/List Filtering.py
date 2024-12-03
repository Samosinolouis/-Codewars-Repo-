'''In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]'''

def filter_list(l):
    return [x for x in l if isinstance(x,int)]

'''import codewars_test as test
import random
from solution import filter_list

@test.describe('Full tests')
def tests():
    @test.it('should work for basic examples')
    def basic_examples():
        test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
        test.assert_equals(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
        test.assert_equals(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')
        test.assert_equals(filter_list(['a', 'b', '1']), [], 'For input ["a", "b", "1"]')
        test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input ["1, 2, "a", "b"]')
    
    @test.it('should work for random inputs')
    def random_tests():
        for _ in range(20):
            input = []
            expected = []
            for _ in range(random.randrange(20)):
                if random.randrange(2) == 0:
                    n = random.randrange(1000)
                    input.append(n)
                    expected.append(n)
                else:
                    if random.randrange(2) == 0: input.append(str(random.randrange(1000)))
                    else: input.append("".join(chr(random.randrange(48,122)) for _ in range(random.randrange(6))))
            test.assert_equals(filter_list(input), expected, f'For input {input}')'''