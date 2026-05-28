'''
Conditional Statements
----------------------
if-->to check whether the statement is true or not.

if-else -->else in the if statement,incase the condition becomes false then it
will enter into fall-back(else),it will execute whatever inside it.
Ex:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

nested if
elif

Vote eligibility
----------------
age_ = int(input("Enter your age: ")
if age_>=18:
    print("You are eligible to vote")
else:
    print(f"You have to wait for {18-age_} more years")

Max no b/w 2 numbers:
---------------------
num1 = int(input("Enter 1st no: "))
num2 = int(input("Enter 2nd no: "))
if num1>=num2:
           print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

Leap year:
----------
year = int(input("Enter year: "))
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(f"{year} is a leap year")
else:
     print(f"{year} is not a leap year")
    
vowel checking
--------------
vowel_ = str(input("Enter a alphabet: "))
if vowel_ in "AEIOUaeiou":
    print(f"{vowel_} is a vowel")
else:
    print(f"{vowel_} is not a vowel")

No is postive or negative
-------------------------
num = int(input("Enter a no: "))
if num>=0:
          print(f"{num} is positive no")
else:
    print(f"{num} is negative no")

Result of marks:
----------------
marks_ = int(input("Enter our marks: "))
stu_name = input("Enter your name ")
if marks_>=45:
             print(f"{stu_name} is passed")
else:
    print(f"{stu_name} is failed")

Divisibility
------------
num = int(input("Enter a no: "))
if num%3 == 0 and num%5 == 0:
          print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

signal
------
Signal_ = int(input("Enter \n1.Red \n2.Green: "))
if Signal_ == 1:
    print("Pls stop")
else:
    print("Go")

'''




