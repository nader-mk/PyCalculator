#Calculator using python
#Nader Mahbub Lhan Nabil
#naderkhan2507@gmail.com
welmassage = "[PyCalculator by Nader Mahbub Khan}"
print(welmassage)
print("=====================================================================")
print("INPUT SECTION")
print("=====================================================================")
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the last number: "))
print("=====================================================================")
#Now I am going to calculate them in many ways
#normal processing
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
remainder = num1%num2
#advanced processing
ave = (num1+num2)/2
square1 = num1**2
square2 = num2**2
cube1 = num1**3
cube2 = num2**3
power1 = num1**num2
power2 = num2**num1

print("Normal Answers:")
print("=====================================================================")
print("Addition of your entered numbers is : ", addition)
print("Subtraction of your entered numbers is : ", subtraction)
print("Multiplication of your entered numbers is : ", multiplication)
print("Divison of your entered numbers is : ", division)
print("Remainder of your entered numbers is : ", remainder)
print("=====================================================================")
print("Advanced Answers:")
print("=====================================================================")
print("Average of your entered numbers is : ", ave)
print("Square of ",num1," (the first number you entered) is : ", square1)
print("Square of ",num2," (the last number your entered) is : ", square2)
print("Cube of ",num1," (the first number you entered) is : ", cube1)
print("Cube of ",num2," (the last number your entered) is : ", cube2)
print("If ",num2,"is the power of ",num1 ,", then the result is : ", power1)
print("If ",num1,"is the power of ",num2 ,", then the result is : ", power2)
print("=====================================================================")
print("Comparing between two numbers that you entered...")
print("=====================================================================")
if num1>num2:
       print(num1," is greater than ",num2,"\n",num2," is less than ",num1)
elif num1<num2:
      print(num2," is greater than ",num1,"\n",num1," is less than ",num2)
elif num1 == num2:
      print("Both ",num1,"and",num2," are equal\n",num1,"=",num2)
else:
       print("Wrong while input or processing\nPlease contact Nader Mahbub Khan Nabil for a solution of this")


