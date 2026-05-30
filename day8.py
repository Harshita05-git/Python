'''
elif-->used for checking multiple conditions.

Examples:
---------
1.Student Grading
-----------------
stu_marks = int(input("Marks: "))
if stu_marks >= 90:
    print("A+")
elif stu_marks >= 80:
    print("A")
elif stu_marks >= 70:
    print("B+")
elif stu_marks >= 60:
    print("B")
elif stu_marks >= 50:
    print("C+")
elif stu_marks >= 35:
    print("Pass")
else:
    print("Fail")

2.Max no b/w 3 numbers:
-----------------------
a,b,c = map(int,input("Enter 3 numbers: ").split())
if a >= b and a >= c:
    print(f"{a} is the max value")
elif b >= a and b >= c:
    print(f"{b} is the max value")
else:
    print(f"{c} is the max value")
                                             or
                                             
a,b,c = map(int,input("Enter 3 numbers: ").split())
print(max(a,b,c))
                                              or
                                              
a,b,c = map(int,input("Enter 3 numbers: ").split())
maximum = max(a,b,c)
print(f"{maximum} is the maximum value")

3.ATM Pin:
-----------
SBI_bank = {"ATM PIN": "6600"}
pin = input("Enter 4 digit ATM PIN: ")
if len(pin) == 4:
    if pin in SBI_bank["ATM PIN"]:
        print("Welcome to SBI ATM")
    else:
        print("Invalid pin")
else:
    print("Enter 4 digit pin")

for statement
-------------
-->Used to iterate over a sequence

any = "Python"
an = [1,2,3,4]
for j in any:
    print(j)

range()
-------
range() is a in-built function used to generate numbers in sequencial manner
Syntax:
range(start,stop,step)

else in for
-----------
-->once the iterations is completed this else will be executed.
Ex:
---
for i in range(1,10):
    print(i)
else:
    print("code is invalid")

break
-----
-->used to exit from the loop based on the condition

for i in range(1,10):
    print(i)
    if i == 5:
       break

continue
--------
-->used to skip the current iteration based on the condition.

for i in range(1,10):
    if i == 7:
       continue
    print(i)

pass
----
-->pass is a null statement-it does nothing.
-->It's used as a placeholder when syntax requires a statement,but you don't want any code to run yet.

for i in range(1,10):
    if i == 5:
       pass


while
------
-->is a combination of for and if

i = 1
while i < 5:
    print(i)
    i += 1
'''
