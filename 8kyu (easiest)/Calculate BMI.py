'''Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"'''

def bmi(weight, height):
    if (weight/height**2 <= 18.5):
        return "Underweight"
    if (weight/height**2 <= 25.0):
        return "Normal"
    if (weight/height**2 <= 30.0):
        return "Overweight"
    if (weight/height**2 > 30):
        return "Obese"

'''@test.describe("BMI Tests")
def fixed_tests():
    @test.it('Fixed Test Cases')
    def basic_test_cases():
        test.assert_equals(bmi(50, 1.80), "Underweight", "For weight = 50 and height = 1.80")
        test.assert_equals(bmi(80, 1.80), "Normal", "For weight = 80 and height = 1.80")
        test.assert_equals(bmi(90, 1.80), "Overweight", "For weight = 90 and height = 1.80")
        test.assert_equals(bmi(100, 1.80), "Obese", "For weight = 100 and height = 1.80")
        test.assert_equals(bmi(50, 1.50), "Normal", "For weight = 50 and height = 1.50")
        
        test.assert_equals(bmi(74, 2.00), "Underweight", "For weight = 74 and height = 2.00")    # 18.5
        test.assert_equals(bmi(54.1, 1.71), "Normal", "For weight = 54.1 and height = 1.71")     # 18.5014
        test.assert_equals(bmi(100, 2.00), "Normal", "For weight = 100 and height = 2.00")       # 25.0
        test.assert_equals(bmi(86.5, 1.86), "Overweight", "For weight = 86.5 and height = 1.86") # 25.003
        test.assert_equals(bmi(120, 2.00), "Overweight", "For weight = 120 and height = 2.00")   # 30.0
        test.assert_equals(bmi(94, 1.77), "Obese", "For weight = 94 and height = 1.77")          # 30.004
    
    @test.it("Random Test Cases")
    def random_tests():
    
        from random import randint
        sol=lambda w,h:(lambda b: "Underweight" if b<= 18.5 else "Normal" if b<= 25.0 else "Overweight" if b<= 30.0 else "Obese")(w/h/h)
        for _ in range(100):
            _bmi, height = randint(1500,4000)/100.0, randint(110,220)/100.0
            weight = round(_bmi * height * height, 1)
            expected = sol(weight, height)
            test.assert_equals(bmi(weight, height), expected, f"For {weight = } and {height = }")'''