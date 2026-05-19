'''
1.Program to convert 24hr clock to normal clock

time_ = input("Enter 24 hours time: ")
parts_ = time_.split(":")
hour_ = int(parts_[0])
min_ = int(parts_[1])
print(f"{time_} is converted into {hour_ - 12}:{min_} pm")


List
------
-->List is a collection of different datatypes.
-->It is represented in [] and seperated by ,
-->mutuable

Methods:
-------
1.append()
-------
-->this is used to add a new item into list and it will add in the last index position.
Syntax:
variable_name.append(item)
Ex:
any = [1,2,3]
any.append(6)
print(any)
any.append([20,5])

2.extend()
--------
-->this is used to add a new iterable into list
and it will add in the last index position,each value or substring is each index in the list.
Syntax:
variable_name.extend(iterable)
Ex:
so = "Python is a language"
print(so.replace("Python","Java"))
print(so)
any = [1,2,3]
any.append(6)
print(any)

Note:
Difference b/w append() and extend():
append()--> adds the entire object as a single element to the list.
extend()--> adds each element seperately from another iterable.

3.pop()
-----
-->used to remove the item from the list,but will mention here index position in the pop method.
Syntax:
variable_name.pop(index position)
Ex:
any = [1,2,3]
any.pop(0)
print(any)

4.remove()
--------
-->used to remove the item from the list,but will mention direct value here in the remove method.
Synatx:
variable_name.remove()
Ex:
any = [1,2,4,6]
any.remove(4)
print(any)

Immutable
---------
-->Could not able to modify on that particular variable.
Ex:int,string

Mutable
-------
-->Can able to modify on that particular variable.
Ex:List
'''
