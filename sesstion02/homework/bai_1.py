height1 = int(input("Your Height(cm) = "))
mass = int(input("Your Weight(kg) = "))
height = height1 / 100
bmi = mass / height**2
print("Your BMI = ",bmi)

if bmi < 16:
    print("Severely underweight")
elif  bmi < 18.5:
    print("Underweight")
elif  bmi < 25:
    print("Normal")
elif  bmi < 30:
    print("Overweight")
elif bmi>=30 :
    print("Obese")