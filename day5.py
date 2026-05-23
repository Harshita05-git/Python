'''
sets
----
-->A set is a collection of unique and unordered elements.
-->Duplicate values are not allowed.
-->Items are not stored in index order.
-->Represented in {}
Ex:
any = {1,2,3,2,4}
print(any)

Methods
-------
1.union()
---------
-->it will give all the values from 2 sets together at once.
Syntax:
variable_name.union(another var)
Ex:
any = {1,2,2,4}
an = {55,78}
print(any | an)
print(any.union(an))

2.intersection()
----------------
-->to get the common elements from both sets.
Syntax:
variable_name.intersection(another var)
Ex:
any = {34,56,99}
an = {89,99,188}
print(any & an)
print(any.intersection(an))

3.difference()
--------------
-->to get the difference values from set.
Syntax:
variable_name.difference(another var)
Ex:
any = {34,56,99}
an = {89,99,188}
print(any - an)
print(any.difference(an))

4.add()
-------
-->to add new elements into the set.
Syntax:
variable_name.add(element)
Ex:
any = {1,22,2,3}
any.add(41)
print(any)

5.update()
----------
-->to add multiple elements into set.
Syntax:
variable_name.upadate([elements])
Ex:
any = {1,22,2,3}
any.update([41,23])
print(any)

6.remove
--------
-->used to remove element from the set but it will throw error{Key error)
if element not in set.
Syntax:
variable_name.remove(element)
Ex:
any = {1,22,2,3}
any.update([44,89])
print(any)

7.discard()
-----------
-->used to remove element from the set but it will never throw error
if element not in set.
Syntax:
variable_name.discard(element)
Ex:
any = {1,22,2,3}
any.discard([44,89])
print(any)

'''












