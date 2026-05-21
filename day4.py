'''
concatination
-------------
-->The (+) for int is for adding values , but for other datatypes it will act as concatinating the datatype.
Ex:
a = 90
b = 8
print(a + b)
any = "Python "
so = "is a language"
print(any + so)
an = [1,2]
am = [3,4]
print(an + am)

tuple
-----
-->Collection of different datatypes and seperated by commas.
-->It is represented in ()
-->Immutable

Methods:
--------
1.count()
-------
-->This is used to count the particular item in the tuple.
Syntax:
variable_name.count(item)
Ex:
some = (1,"Python",[5,11],(8,55),"Python")
print(some.count("Python"))

2.index()
-------
-->used to find out the index position of the item, and only gives the first  occurrance.
some = (1,"Python",[5,11],(8,55))
print(some.index("Python"))
Ex:
data = (
    10,
    "Java",
    (
        5,
        9,
        (22, "this is tuple practice", 77),
        "Tuple is immutable",
        100
    ),
    45
)
print(data[2][2][1][0])
print(data[2][3][0])
print(data[2][3][9])
--------------------
data = [
    5,
    "Python",
    (
        10,
        [20, 30, (40, "hello world", 60)],
        "Data Structures"
    ),
    "End"
]
print(data[2][1][2][1][0])
print(data[2][2][0])
print(data[2][1][2][2])
-----------------------
data = [
    "start",
    (
        10,
        [
            "A",
            (5, "keep", [1, 2, ("going", "Python", 99)]),
            "X"
        ],
        "middle"
    ),
    [
        (100, "you"),
        ("are", [("doing", "great"), "!!!"]),
        "Z"
    ]
    "end"
]
print(data[1][1][1][2][2][1][0])
print(data[1][1][1][2][2][0][0])
print(data[2][1][1][0][0][0])
print(data[2][0][1])

Dictionary
----------
-->Dict is a key : value pair, key and value is seperated by : and pair is seperated by comma
-->Represented by {}
Syntax:
dictionary_name = {
                     key1: value1,
                     key2: value2
                  }

Ex:
harshi_details = {"Name" : "Harshi",
                  1:2,
                  (1,2):[3,4]}
print(type(harshi_details))

-->in key you can only use strings,int values,and tuple i.e the ones which are immutable
whereas in value you can all of them including list which is mutable.

Methods
-------
1.keys()
------
-->used to get all keys from the dictionary.
Syntax:
dict.key()
Ex:
harshi_details = {"Name" : "Harshi",
                   "age" : 19,
                   "MobN" : "7993813553"
                   }
print(harshi_details.keys())

2.values()
--------
-->used to get all values from the dict.
Syntax:
dict.values()
Ex:
harshi_details = {"Name" : "Harshi",
                   "age" : 19,
                   "MobN" : "7993813553"
                   }
print(harshi_details.values())

3.items()
-------
-->used to get key and value together
Syntax:
dict.items()
Ex:
harshi_details = {"Name" : "Harshi",
                   "age" : 19,
                   "MobN" : "7993813553"
                   }
print(harshi_details.items())
print(harshi_details["age"])

4.update()
--------
-->used to add a new key:value pair into dictionary.
Syntax:
dict.update({key:value})
Ex:
harshi_details = {"Name" : "Harshi",
                   "age" : 19,
                   "MobN" : "7993813553"
                   }
harshi_details.update({"Aadhar" : 465972819012})
print(harshi_details)

clear()
-------
-->used to remove all the items in the dictionary.
Ex:
harshi_details = {"Name" : "Harshi",
                   "age" : 19,
                   "MobN" : "7993813553"
                   }
harshi_details.clear()
print(harshi_details)
'''




                           


