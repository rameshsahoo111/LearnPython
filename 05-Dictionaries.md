# Dictionaries in Python

> Python’s official documentation defines a dictionary: an associative array, where arbitrary keys are mapped to values. The keys can be any object with **__hash__()** and **__eq__()** methods.

<br />


Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.


<br />


This section will serve as a brief introduction to dictionaries and consist of:

    1.) Constructing a Dictionary
    2.) Accessing objects from a dictionary
    3.) Operators and Built-in Functions
    4.) Nesting Dictionaries
    5.) Dictionary Methods
    6.) Iterating dictionary


<br />

There are a couple points to keep in mind:

1. ) Dictionaries map keys to values and store them in an array or collection.

2. ) The keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.



### Constructing a Dictionary

- Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.
- An item has a key and a corresponding value that is expressed as a pair (key: value).
- While the values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:

```python
>>> d = {<key1>: <value1>, <key2>: <value2>, . ., <key3>: <valu3>}
```


The following defines a dictionary that maps a location to the name of its corresponding Major League Baseball team:

```python
>>> MLB_team = {
...     'Colorado' : 'Rockies',
...     'Boston'   : 'Red Sox',
...     'Minnesota': 'Twins',
...     'Milwaukee': 'Brewers',
...     'Seattle'  : 'Mariners'
... }
```

![image.png](attachment:image.png)

<br />

<br />


MLB_team can then also be defined this way:

```python
>>> MLB_team = dict([
...     ('Colorado', 'Rockies'),
...     ('Boston', 'Red Sox'),
...     ('Minnesota', 'Twins'),
...     ('Milwaukee', 'Brewers'),
...     ('Seattle', 'Mariners')
... ])
```

If the key values are simple strings, they can be specified as keyword arguments. So here is yet another way to define MLB_team:


```python
>>> MLB_team = dict(
...     Colorado='Rockies',
...     Boston='Red Sox',
...     Minnesota='Twins',
...     Milwaukee='Brewers',
...     Seattle='Mariners'
... )
```

Once you’ve defined a dictionary, you can display its contents, the same as you can do for a list. All three of the definitions shown above appear as follows when displayed:

```python

>>> type(MLB_team)
<class 'dict'>

>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}

```

</br>

The entries in the dictionary display in the order they were defined. But that is irrelevant when it comes to retrieving them. Dictionary elements are not accessed by numerical index:


```python
>>> MLB_team[1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    MLB_team[1]
KeyError: 1
```



```python
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
```

### Accessing objects from a dictionary


```python
# Call values by their key
my_dict['key2']
```




    'value2'



Its important to note that dictionaries are very flexible in the data types they can hold. For example:


```python
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
```


```python
# Let's call items from the dictionary
my_dict['key3']
```




    ['item0', 'item1', 'item2']




```python
# Can call an index on that value
my_dict['key3'][0]
```




    'item0'




```python
# Can then even call methods on that value
my_dict['key3'][0].upper()
```




    'ITEM0'



We can affect the values of a key as well. For instance:


```python
my_dict['key1']
```




    123




```python
# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
```


```python
#Check
my_dict['key1']
```




    0



>**A quick note**, Python has a built-in method of doing a self subtraction or addition (or multiplication or division). We could have also used += or -= for the above statement. For example:


```python
# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
my_dict['key1']
```




    -123



We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:


```python
# Create a empty dictionary
d = {}
```


```python
# Create a new key through assignment
d['animal'] = 'Dog'
```


```python
# Can do this with any object
d['answer'] = 42
```


```python
#Show
d
```




    {'animal': 'Dog', 'answer': 42}



### Modifying Values and Keys

The values, for example, can be modified whenever you need, but you’ll need to use the original dictionary and the key that maps the value you want to modify:



```python
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
```


```python
prices
```




    {'apple': 0.4, 'orange': 0.35, 'banana': 0.25}




```python
## Apply 10% discount to price 

for k,v in prices.items():
    prices[k] = round(v * 0.9, 2) ## Apply 10% discount
    
print(prices)

```

    {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}



```python
prices
```




    {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}



### Operators and Built-in Functions

Built-in functions that can be used with strings, lists, and tuples. Some of these work with dictionaries as well.

For example, the **in** and **not** in operators return **True or False** according to whether the specified operand occurs as a key in the dictionary:




```python
d = dict(Mango=20.30,Appel=30.20)
```


```python
'Mango' in d
```




    True




```python
'Text' in d
```




    False



## Nesting with Dictionaries

Hopefully you're starting to see how powerful Python is with its flexibility of nesting objects and calling methods on them. Let's see a dictionary nested inside a dictionary:


```python
# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
```

Wow! That's a quite the inception of dictionaries! Let's see how we can grab that value:


```python
# Keep calling the keys
d['key1']['nestkey']['subnestkey']
```




    'value'




```python
## An another example of nested dictionary 
d = {'person':{'village':{'name':'Mumbai','Address':'301, Sector 1, Jain Temple, Mumbai - 001'}}}
```


```python
d['person']
```




    {'village': {'name': 'Mumbai',
      'Address': '301, Sector 1, Jain Temple, Mumbai - 001'}}




```python
d['person']['village']
```




    {'name': 'Mumbai', 'Address': '301, Sector 1, Jain Temple, Mumbai - 001'}




```python
d['person']['village']['name']
```




    'Mumbai'




```python
d['person']['village']['Address']
```




    '301, Sector 1, Jain Temple, Mumbai - 001'




```python
print('Village of person is {0} and address is {1}'.format(d['person']['village']['name'],d['person']['village']['Address']))
```

    Village of person is Mumbai and address is 301, Sector 1, Jain Temple, Mumbai - 001


## Python Dictionary Methods

### Python Dictionary keys()

`dict.keys()`

- The **keys()** method returns a view object that displays a list of all the keys in the dictionary

- keys() doesn't take any parameters.

- keys() returns a view object that displays a list of all the keys.

- When the dictionary is changed, the view object also reflects these changes.




```python
# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}
```


```python
# Method to return a list of all keys 
d.keys()
```




    dict_keys(['key1', 'key2', 'key3'])



### dict.values()

`dictionary.values()`

- The values() method returns a view object that displays a list of all the values in the dictionary.

- values() method doesn't take any parameters.

- values() method returns a view object that displays a list of all values in a given dictionary.





```python
# Method to grab all values
d.values()
```




    dict_values([1, 2, 3])



### dict.items()

`dictionary.items()`

- The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.

- items() method is similar to dictionary's viewitems() method in Python 2.7.

- items() method doesn't take any parameters.



```python
# Method to return tuples of all items  (we'll learn about tuples soon)
d.items()
```




    dict_items([('key1', 1), ('key2', 2), ('key3', 3)])



### dict.update()

`dict.update([other])`

> Merges a dictionary with another dictionary or with an iterable of key-value pairs.



- The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

- The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).

- If update() is called without passing parameters, the dictionary remains unchanged.

- It doesn't return any value (returns None).


```python
# Empty dict
d = {}

d1 = {'Mango':10,'Appel':20,'Banana':10}
```


```python
d.update(d1)
```


```python
d
```




    {'Mango': 10, 'Appel': 20, 'Banana': 10}




```python
d1
```




    {'Mango': 10, 'Appel': 20, 'Banana': 10}




```python
d.update(Guava = 30)
```


```python
## Updated 
d
```




    {'Mango': 10, 'Appel': 20, 'Banana': 10, 'Guava': 30}




```python
## d1 remains same
d1
```




    {'Mango': 10, 'Appel': 20, 'Banana': 10}




```python
d.update(name = 'name')
```


```python
d 
```




    {'Mango': 10, 'Appel': 20, 'Banana': 10, 'Guava': 30, 'name': 'name'}




```python
n = 10 

d.update(r = n)
```


```python
d
```




    {'Mango': 10, 'Appel': 20, 'Banana': 10, 'Guava': 30, 'name': 'name', 'r': 10}




```python
## for loop dictionary update example

master_dist = {'Mango': 10, 'Appel': 20, 'Banana': 10, 'Guava': 30, 'name': 'name'}
d = {}

for k,v in master_dist.items():
    d[k] = v
        
print(d.items())

```

    dict_items([('Mango', 10), ('Appel', 20), ('Banana', 10), ('Guava', 30), ('name', 'name')])



```python
## update() When Tuple is Passed
d = {'x': 2}

d.update(y = 3, z = 0)
print(d)
```

    {'x': 2, 'y': 3, 'z': 0}


### dict.setdefault()

`dict.setdefault(key[, default_value])`


The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.

#### setdefault() takes a maximum of two parameters:

- key - the key to be searched in the dictionary
- default_value (optional) - key with a value default_value is inserted to the dictionary if the key is not in the dictionary. If not provided, the default_value will be None.

#### Returns
- value of the key if it is in the dictionary
- None if the key is not in the dictionary and default_value is not specified
- default_value if key is not in the dictionary and default_value is specified



```python
## Example 1 
person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)


```

    person =  {'name': 'Phill', 'age': 22}
    Age =  22



```python
## How setdefault() works when key is not in the dictionary?

person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)


```

    person =  {'name': 'Phill', 'salary': None}
    salary =  None
    person =  {'name': 'Phill', 'salary': None, 'age': 22}
    age =  22


### dict.fromkeys()

`dictionary.fromkeys(sequence[, value])`

The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.

#### fromkeys() Parameters

- sequence - sequence of elements which is to be used as keys for the new dictionary
- value (Optional) - value which is set to each each element of the dictionary

#### Return value from fromkeys()**

- fromkeys() method returns a new dictionary with the given sequence of elements as the keys of the dictionary.

- If the value argument is set, each element of the newly created dictionary is set to the provided value.

- If no value is provided, default value is set to **None**


```python
## Example 1: Create a dictionary from a sequence of keys
person_details_list = ['Name','Contact Number','City']
person_details_dict = dict.fromkeys(person_details_list)
print(person_details_dict)
```

    {'Name': None, 'Contact Number': None, 'City': None}



```python
## Example 2: If you want set a default for all keys
person_details_list = ['Name','Contact Number','City']
V = 'xxxxxx'

person_details_dict = dict.fromkeys(person_details_list,V)
print(person_details_dict)


```

    {'Name': 'xxxxxx', 'Contact Number': 'xxxxxx', 'City': 'xxxxxx'}



```python
## Example 3: Create a dictionary from mutable object list

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)

# Replace value
value.clear()
value.append(3)
print(vowels)
```

    {'o': [1], 'i': [1], 'a': [1], 'u': [1], 'e': [1]}
    {'o': [1, 2], 'i': [1, 2], 'a': [1, 2], 'u': [1, 2], 'e': [1, 2]}
    {'o': [3], 'i': [3], 'a': [3], 'u': [3], 'e': [3]}


If value is a mutable object (whose value can be modified) like list, dictionary, etc., when the mutable object is modified, each element of the sequence also gets updated.

This is because each element is assigned a reference to the same object (points to the same object in the memory).

To avoid this issue, we use dictionary comprehension.



```python
## Example 3 --> Don't change value
#vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)
```

    {'o': [1], 'i': [1], 'a': [1], 'u': [1], 'e': [1]}
    {'o': [1], 'i': [1], 'a': [1], 'u': [1], 'e': [1]}



```python
## Example 4: Populate both key and values
person_details_list = ['Name','Contact Number','City']
person_value = ['Python','Community','world']
person_dict = dict.fromkeys(person_details_list)

c = 0
for k in person_dict.keys():
    person_dict[k] = person_value[c]
    c += 1

print(person_dict)

```

    {'Name': 'Python', 'Contact Number': 'Community', 'City': 'world'}


### dict.get()

`dict.get(key[, value])`

The **get()** method returns the value for the specified key if key is in dictionary.

#### get() method takes maximum of two parameters:

- key - key to be searched in the dictionary
- value (optional) - Value to be returned if the key is not found. The default value is None.


#### Return Value from get()

get() method returns:

- the value for the specified key if key is in dictionary.
- None if the key is not found and value is not specified.
- value if the key is not found and value is specified.

> Note: **get()** method can be replaced with dict['key']. With dict['key'], if the key is not found in the dictionary, dict method will throw **KeyError** exception. With get() method we can return a default value if the key is not found. 


```python
## Example 1: How get() works for dictionaries?
d = {'Mango': 10, 'Appel': 20, 'Banana': 10, 'Guava': 30, 'name': 'name'}
```


```python
print(d.get('Ramesh'))
```

    None



```python
## with dict['key'], we can see KeyError execption
d['notfound']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-35-f36334b66dc6> in <module>
          1 ## with dict['key'], we can see KeyError execption
    ----> 2 d['notfound']
    

    KeyError: 'notfound'



```python
## Return a default value where key is not found
d = {'Mango': 10, 'Appel': 20, 'Banana': 10, 'Guava': 30, 'name': 'name'}

d.get('nuts','Jamun')
```




    'Jamun'




```python
## Example 2:
    
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 20.30))
```

    Name:  Phill
    Age:  22
    Salary:  None
    Salary:  20.3


### dict.pop()

`dictionary.pop(key[, default])`

The pop() method removes and returns an element from a dictionary having the given key.

#### pop() Parameters

pop() method takes two parameters:

- key - key which is to be searched for removal
- default - value which is to be returned when the key is not in the dictionary


#### Return value from pop()

The pop() method returns:

- If key is found - removed/popped element from the dictionary
- If key is not found - value specified as the second argument (default)
- If key is not found and default argument is not specified - KeyError exception is raised



```python
## Example 1 -- Pop an item 
person = {'name': 'Phill', 'age': 22}

# Popping age
person.pop('age')
```




    22




```python
# Age has been popped properly 
person
```




    {'name': 'Phill'}




```python
## Example 2 -- Pop an item which doesn't exist
person = {'name': 'Phill', 'age': 22}

# Python doesn't exist hence we'll get key error exception
person.pop('Python')
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-44-da83ec477fd2> in <module>
          1 ## Example 2 -- Pop an item which doesn't exist
          2 person = {'name': 'Phill', 'age': 22}
    ----> 3 person.pop('Python')
    

    KeyError: 'Python'



```python
## Pop an item which doesn't exist. Return the default value instead of Keyerror exception 
print(person)
print(person.pop('Python','Not Found'))
```

    {'name': 'Phill', 'age': 22}
    Not Found


### dict.popitem()

`dict.popitem()`

The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.

#### Parameters for popitem() method

- The popitem() doesn't take any parameters.

#### Return Value from popitem() method

- The popitem() method removes and returns the (key, value) pair from the dictionary in the Last In, First Out (LIFO) order.

- Returns the latest inserted(removed) element (key,value) pair from the dictionary.

- Removes the returned element pair from the dictionary.

> Note: Before Python 3.7, the popitem() method returned and removed an arbitrary element (key, value) pair from the dictionary.


```python
## Example
person = {'name': 'Phill', 'age': 22,'City':'Mumbai'}
```


```python
person.popitem()
```




    ('City', 'Mumbai')




```python
# The last element has been popped
person
```




    {'name': 'Phill', 'age': 22}



### dict.copy()

- They copy() method returns a shallow copy of the dictionary.
- copy() method doesn't take any parameters.
- This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.



```python
"""
Example: 1 
copying a dictionary to another variable also leaves a chance of the original dictionary getting modified
if there is a modification is made to the new copied dictionary. 
"""

d = {'Appel':20,'Mango':30}
print(f"Original d = {d}")

d1 = d
d1.update(Banana = 50)
d1.update(Appel = 300)

print(f"d1 = {d1}\nd = {d}")
```

    Original d = {'Appel': 20, 'Mango': 30}
    d1 = {'Appel': 300, 'Mango': 30, 'Banana': 50}
    d = {'Appel': 300, 'Mango': 30, 'Banana': 50}



```python
"""
Example: 2
Avoid original dictionary content getting modified with dict.copy() method 
"""
d = {'Appel':20,'Mango':30}
print(f"Original d = {d}")

d1 = d.copy()
d1.update(Banana = 50)
d1.update(Appel = 300)

print(f"d1 = {d1}")
print(f"Original d = {d}")

```

    Original d = {'Appel': 20, 'Mango': 30}
    d1 = {'Appel': 300, 'Mango': 30, 'Banana': 50}
    Original d = {'Appel': 20, 'Mango': 30}


### dict.clear()  

- The clear() method removes all items from the dictionary.
- clear() method doesn't take any parameters.
- clear() method doesn't return any value (returns None).


```python
#Polulate dictionary 
d = {'Appel':20,'Mango':30}
print(d)

#Clear Dictionary 
d.clear()
print('Empty dict:',d)

```

    {'Appel': 20, 'Mango': 30}
    Empty dict: {}


### Iterating dictionary

Using for loop, we can iterate dictionary elements as per our requirement. 


```python
my_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

## Print key only
for key in my_dict:
    print(key)
```

    color
    fruit
    pet



```python
## Print both key and value with tuple unpacking
for key,val in my_dict.items():
    print(key,' : ',val)
```

    color  :  blue
    fruit  :  apple
    pet  :  dog



```python
## Print both key and value in a different way
for key in my_dict:
    print(key,' -> ',my_dict[key])

```

    color  ->  blue
    fruit  ->  apple
    pet  ->  dog



```python
## iterating through item 
for item in my_dict.items():
    print(item)

```

    ('color', 'blue')
    ('fruit', 'apple')
    ('pet', 'dog')


### Reference
- https://realpython.com/python-dicts
- https://www.programiz.com/python-programming/methods/dictionary
- https://www.udemy.com/complete-python-bootcamp
- My own notes 


```python

```
