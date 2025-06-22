#Control statements

#(num = 56-46
#if num > 10:
    #print("This number is greater than ten")
#elif num == 10:
    #print("This number is equal to ten")
#else:
    #print("This number is less than ten")
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num2, " is greater than ", num1)
else:
    print("These numbers are equal")