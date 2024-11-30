'''Oh no!
Some really funny web dev gave you a sequence of numbers from his API response as an sequence of strings!

You need to cast the whole array to the correct type.

Create the function that takes as a parameter a sequence of numbers represented as strings and outputs a sequence of numbers.

ie:["1", "2", "3"] to [1, 2, 3]

Note that you can receive floats as well.'''

def to_float_array(arr): 
    for i in range(len(arr)):
        arr[i]=(float(arr[i]))
    return arr

'''
Test Case:
import codewars_test as test
from solution import to_float_array

@test.describe("Example Tests")
def test_group():
    @test.it('Example Test Case')
    def test_case():
        test.assert_equals(to_float_array(["1.1", "2.2", "3.3"]), [1.1, 2.2, 3.3])
             
             
from random import randint, uniform
             
@test.describe('Random Tests')
def random_tests():
             
    def generate_random_case(): 
        def random_float_str(x): 
             return str(round((uniform(-10, 10)), randint(1, 3)))
        return list(map(random_float_str, range(randint(1, 20))))

    def _to_float_array_ref(arr): 
        return list(map(float, arr))

    def _do_one_test():
        arr = generate_random_case()
        expected = _to_float_array_ref(arr)
        actual = to_float_array(arr)
        test.assert_equals(actual, expected)

    @test.it('Random Test Cases')
    def random_test_cases():
        for _ in range(100):
            _do_one_test()'''