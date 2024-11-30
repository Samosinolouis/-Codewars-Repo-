'''Bob needs a fast way to calculate the volume of a cuboid with three values: the length, width and height of the cuboid. Write a function to help Bob with this calculation.'''

def get_volume_of_cuboid(length, width, height):
    return length * width *height

'''
TEST CASE:
import codewars_test as test
try:
    from solution import get_volume_of_cuboid
except:
    from solution import getVolumeOfcuboid as get_volume_of_cuboid

    
@test.describe('Testing...')
def _():
    
    @test.it('Sample tests')
    def _():   
        test.assert_equals(get_volume_of_cuboid(1, 2, 2), 4)
        test.assert_equals(get_volume_of_cuboid(6.3, 2, 5), 63)
        
        
    @test.it('Random tests')
    def _():
        from random import randrange as rand
        for _ in range(50):
            a,b,c = (rand(0,100) for _ in range(3))
            exp = a*b*c
            test.assert_equals(get_volume_of_cuboid(a,b,c), exp)'''