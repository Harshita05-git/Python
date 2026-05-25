'''
Type conversions
----------------
int-->

any = 98
us = str(any)
on = float(any)
print(type(on))
print(type(us))

str-->

an = "90"
Ear = int(an)
print(Ear)
print(type(Ear))
hi = list(an)
print(hi)
print(type(hi))
con = tuple(an)
print(con)
print(type(con))

float-->

car = 78.99
print(int(car))
print(type(str(car)))

List-->

Any = [5,11]
print(str(Any))
print(tuple(Any))

tuple-->

how = (4,6)
print(list(how))
print(str(how))

int as a user-input
-------------------
num = int(input("Enter a no:"))
print(89+num)

str as a user-input
-------------------
some = str(input("Write a text: "))
print(some)

list as a user-input
-------------------
any = list(map(int,input("Enter numbers: ").split()))
print(any)

tuple as a user-input
-------------------
any = tuple(map(int,input("Enter numbers: ").split()))
print(any)

num = eval(input("Enter: "))
print(type(num))

'''
