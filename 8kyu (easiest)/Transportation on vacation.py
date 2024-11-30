'''After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).'''

def rental_car_cost(d):
    if d<3:
        return d*40
    elif d<7 and d>3:
        return d*40-20
    else:
        return d*40-50

'''
TEST CASE:
import codewars_test as test
from solution import rental_car_cost

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(rental_car_cost(1),40)
        test.assert_equals(rental_car_cost(4),140)
        test.assert_equals(rental_car_cost(7),230)
        test.assert_equals(rental_car_cost(8),270)
        
@test.describe("Random Tests")
def random_tests():
    #############
    def rental_car_cost_solution(d):
        costs = 40 * d
        if d >= 7:
            costs -= 50
        elif d >= 3:
            costs -= 20   
        return costs
    #############
    
    from random import randint
            
    for _ in range(0, 200):
        d = randint(0, 5000)
        r = rental_car_cost_solution(d)
        @test.it(f"testing for rental_car_cost({d})")
        def test_case():
            test.assert_equals(rental_car_cost(d), r)'''