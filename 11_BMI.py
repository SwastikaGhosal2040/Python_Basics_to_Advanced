# calculate BMI = weight in Kg / (height * height ) in meter
weight = float(input('Enter weight in kg = '))
height = float(input('Enter height in meter = '))
BMI = round(weight / (height ** 2 ))
print('The BMI is = ',BMI)
if BMI<18.5:
    print(f'Your BMI is {BMI} and you are underweight.')
elif BMI<25:
    print(f'Your BMI is {BMI} and you have a normal weight.')
elif BMI<30:
     print(f'Your BMI is {BMI} and you are overweight.')
elif BMI<35:
     print(f'Your BMI is {BMI} and you are obase.')
else:
     print(f'Your BMI is {BMI} and you are clinically obase.')