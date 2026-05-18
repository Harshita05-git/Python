'''
Operators
----------
1.Arithmetic operator
---------------------
+,-,*,%,/,//,**

Ex:
print(4*5)
print(4%5==0)
print(10**2)
print(10/2)
print(35.20//5)
print(10%2==0)

2.Assignment operator
---------------------
=, +=, -=, %=, *=

Ex:
count = 0
for j in range(1,10):
    count += 1
print(count)

3.Comparison operator
---------------------
==, !=, > ,<, >=, <=

Ex:
a=5
b=11
print(a == b)

4.Logical operator
------------------
and-->this operator is used to combine and check two conditions.
It returns:
True->if both conditions are true
False->if any one condition is false.

Syntax:
condition1 and condition2

Ex1:
a=10
b=5
print(a>5 and b<10)
Ex2:
a = 15
if a%3 == 0 and a%5 == 0:
   print("True")

or->this operator is used to combine and check two conditions.
It returns:
True->if atleast one condition is true
False->only if both conditions is false.

Syntax:
condition1 or condition2

not->Used to reverse the result of the condition.
It returns:
True->if the condition is false.
False->if the condition is true.
Syntax:
not condition

5.Membership operator
---------------------
in
not in
Ex:
a = 7
b [1,3]
print(a not in b)

6.Identity operator
-------------------
is, is not 
is--> this operator is used to check whether two variables refer to the same object in the memory.
It returns:
True-> if both variables point to the same object.
False->otherwise

NOTE:
Difference b/w == and is:
== operator checks if the values are equal or not.
is operator checks if they are in the same object identity.

Ex:
a = [1,2]
b = [1,2]
c = a
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(a is c)
print(a is not b)

7.Bitwise operator
------------------
&,|,<<,>>
0101
0011
----
0001
Ex:
print(5|3)

                                       Strings
String is sequence of characters enclosed in '',"",'''''' and string is immutable.
methods
-------
replace()
---------
-->Used to replace with a new substring.
Syntax:
variable_name.replace("old string","new string")
Ex:
any = "Python is a language"
print(any.replace("Python","Java"))
print(any)

split()
-------
-->Used to seperate into parts and it will split based on the substring where before substring is one index and after is another index
in the list.
Syntax:
variable_name.split("substring")
Ex:
any = "Python is a language"
print(any.split("is"))

len()
-----
-->get the number of items, substring
Syntax:
len(variable_name)
Ex:
any = "Python is a language"
print(len(any))

slicing
--------
-->can give the access to get particular index from the string.
Syntax:
variable_name[starting index : ending index]
Ex:
any = "Python is a language"
print(any[3:11])

indexing
--------
-->used to get the substring present in that index position 
Syntax:
variable_name[index position]
Ex:
any = "Python is a language"
print(any[7])
print(any.index("ang"))
'''










