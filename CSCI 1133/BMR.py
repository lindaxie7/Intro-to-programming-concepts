weight = float(input("Input weight in pounds: "))
height = float(input("Input height in inches: "))
age = float(input("Input age in years: "))
sex = input("Input M or F: ")
BMR = 0
if sex == 'F':
   BMR = 655 + (4.3 * weight ) + (4.7 * height) - (4.7 * age)
elif sex == 'M':
   BMR = 66 + (6.3 * weight ) + (12.9 * height ) - (6.8 * age )
print('number of chocolate bars is: ',  BMR//230)
