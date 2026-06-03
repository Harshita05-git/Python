'''
for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j)

num = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num} x {i} = {i*num}")

Palindrome:
-----------
so = input("Enter a word: ")
empty_str = ""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")
   
so = input("Enter a word: ")
print(so[::-1])

Armstrong no:
-------------
-->A number that is equal to the sum of its digits raised to the power of the number of digits.

num = int(input("Enter a number: ")
armstrong_ = 0
length_ = len(str(num))
print(length_)
for i in str(num):
    armstrong_ += int(i) ** length_
if num == armstrong_:
    print(f"{num} is an armstrong no")
else:
    print(f"{num} is not an armstrong no")


Perfect number:
---------------
A Perfect Number is a number that is equal to the sum of its proper divisors (all positive divisors except the number itself).

num = int(input("Enter a number: "))
per_nu = 0
for j in range(1,num):
          if num % j == 0:
             per_nu += j
if per_nu == num:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not a perfect number")

Prime number:
-------------
A Prime Number is a number that has exactly two factors.

num = int(input("Enter a number: "))
count = 0
for k in range(1,num+1):
    if num % k == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

--------------------------------------
num = list(map(int,input().split()))
even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers: ",even)
print("Odd numbers: ",odd)
print("Maximum:",max(num))
print("Minimum:",min(num))
-----------------------------------------
city = tuple(map(str,input().split()))
print(city)
-------------------------------------------
n = int(input())
student = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    student[name] = marks
print(student)
--------------------------------------------
an = list(map(int,input().split()))
any_ = set(an)
print(any_)
------------------------------------------------
city = tuple(map(str,input("Tuple:").split()))
product = {}
for i in range(int(input())):
    name = input()
    price = int(input())
    product[name] = price
print(city)
print(product)
a = list(map(int,input("Set values: ").split()))
b = set(a)
print("Set:",b)
-------------------------------------------------
Salary = float(input())
if Salary >= 70000:
   Bonus = Salary*0.20
   print("Bonus:",Bonus)
elif Salary >= 50000:
   Bonus = Salary*0.15
   print("Bonus:",Bonus)
elif Salary >= 30000:
   Bonus = Salary*0.10
   print("Bonus:",Bonus)
else:
   Bonus = Salary*0.05
   print("Bonus:",Bonus)
----------------------------------------------------
star_ = 5
for i in range(1,star_+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
--------------------------------------------------
pattern_ = 5    
for i in range(1,pattern_+1):
    for j in range(1,i+1):
        print(chr(64+j),end = "")
    print()
---------------------------------------------------
star_ = 5
count = 0
for i in range(1,star_+1):
    for j in range(1,i+1):
        count += 1
        print(count,end = " ")
    print()
---------------------------------------------------
star_ = 5
for i in range(1,star_+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
-------------------------------------------------
star_ = 5
for i in range(star_,0,-1):
    for j in range(i):
        print("*",end="")
    print()
-------------------------------------------------
star_ = 5
for i in range(star_,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
---------------------------------------------------
'''
        

    
    
        

    








