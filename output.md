❯ python
Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = '12'
>>> a
'12'
>>> a - 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> int(a)
12
>>> int(a) - 3
9
>>> word = 'python'
>>> word[0]
'p'
>>> word[5]
'n'
>>> word[-2]
'o'
>>> word[-1]
'n'
>>> word[-6]
'p'
>>> word[0:2]
'py'
>>> word
'python'
>>> word[0:]
'python'
>>> word[:-6]
''
>>> word[:-1]
'pytho'
>>> word[:0]
''
>>> word[:]
'python'
>>> word[23]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> word[:23]
'python'
>>> word[10:23]
''
>>> word
'python'
>>> word[0] = 'j'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> print('j', word[1:])
j ython
>>> print('j' + word[1:])
jython
>>> print(f'j')
j
>>> print(f'j${word[1:]}')
j$ython
>>> print(f'j{word[1:]}')
jython
>>> print(f'j{word}')
jpython
>>> fruits = ['orange', 'apple', 'pear']
>>> ['orange', 'apple', 'pear']
['orange', 'apple', 'pear']
>>> fruits
['orange', 'apple', 'pear']
>>> fruits.count('apple')
1
>>> fruits.count('banana')
0
>>> fruits.reverse()
>>> fruits
['pear', 'apple', 'orange']
>>> fruits.append('banana')
>>> fruits
['pear', 'apple', 'orange', 'banana']
>>> fruits.reverse()
>>> fruits
['banana', 'orange', 'apple', 'pear']
>>> fruits.append('orange')
>>> fruits
['banana', 'orange', 'apple', 'pear', 'orange']
>>> basket = {'apple', 'orange', 'apple', 'banana'}
>>> basket
{'apple', 'orange', 'banana'}
>>> emptyFruit = []
>>> basketEmpty = set()
>>> basketEmpty.add('orange')
>>> basketEmpty
{'orange'}
>>> basketEmpty.add('banana')
>>> basketEmpty
{'banana', 'orange'}
>>> basketEmpty.add('orange')
>>> basketEmpty
{'banana', 'orange'}
>>> 'orange' in basketEmpty
True
>>> 'pear' in basketEmpty
False
>>> listOfFruits = []
>>> listOfFruits.count('apple')
0
>>> listOfFruits.append('apple')
>>> listOfFruits.count('apple')
1
>>> listOfFruits
['apple']
>>> listOfFruits.append('orange')
>>> listOfFruits
['apple', 'orange']
>>> listOfFruits.count('apple')
1
>>> listOfFruits.append('apple')
>>> listOfFruits
['apple', 'orange', 'apple']
>>> listOfFruits.count('apple')
2
>>> basketEmptyNotDefined.add('fruit')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'basketEmptyNotDefined' is not defined
>>> mySuperBasket = set()
>>> myPile = []
>>> myPile.append('banana')
>>> myPile.append('kiwi')
>>> myPile.append('orange')
>>> myPile
['banana', 'kiwi', 'orange']
>>> myPile.pop()
'orange'
>>> myPile
['banana', 'kiwi']
>>> myPile.pop()
'kiwi'
>>> myPile
['banana']
>>> myPile.pop()
'banana'
>>> myPile
[]
>>> myPile.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> from collections import deque
>>> queue = deque(['kiwi', 'banana', 'orange'])
>>> queue
deque(['kiwi', 'banana', 'orange'])
>>> queue.popleft()
'kiwi'
>>> queue
deque(['banana', 'orange'])
>>> queue.popleft()
'banana'
>>> queue
deque(['orange'])
>>> queue.popleft()
'orange'
>>> queue
deque([])
>>> queue.popleft()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from an empty deque
>>>  queue
  File "<stdin>", line 1
    queue
IndentationError: unexpected indent
>>> myTuple = 12, 54, 'hello'
>>> myTuple
(12, 54, 'hello')
>>> myTuple[0]
12
>>> myTuple[0] = 24
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> uTuple = myTuple, (1, 2, 3)
>>> uTuple
((12, 54, 'hello'), (1, 2, 3))
>>>  strTuple = 'hello'
  File "<stdin>", line 1
    strTuple = 'hello'
IndentationError: unexpected indent
>>> strTuple = 'hello'
>>> strTuple = 'hello', 'tout', 'le', '
monde'
>>> strTuple
('hello', 'tout', 'le', 'monde')
>>> singletonTuple = 'hello',
>>> singletonTuple
('hello',)
>>> tuple3Items = 12, 14, 15
>>> tuple3Items[1] = 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tuple3Itemsv2 = 12, 18, 15
>>> tuple3Items = 12, [14], 15
>>> tuple3Items[1] = list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tuple3Items[1]
[14]
>>> tuple3Items[1][0] = 18
>>> tuple3Items
(12, [18], 15)
>>> tel = {'jack': 0432, 'sape': 4143}
  File "<stdin>", line 1
    tel = {'jack': 0432, 'sape': 4143}
                   ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> tel = {'jack': 432, 'sape': 4143}
>>> tel
{'jack': 432, 'sape': 4143}
>>> tel['guido'] = 1232
>>> tel
{'jack': 432, 'sape': 4143, 'guido': 1232}
>>> tel['jack']
432
>>> tel['jack'] = 4444
>>> tel['jack']
4444
>>> tel
{'jack': 4444, 'sape': 4143, 'guido': 1232}
>>> del tel['sape']
>>> tel
{'jack': 4444, 'guido': 1232}
>>> del tel['sape']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'sape'
>>> list(tel)
['jack', 'guido']
>>> tel[141] = 'hola'
>>> tel
{'jack': 4444, 'guido': 1232, 141: 'hola'}
>>> tel[('test', 12)] = 'hola'
>>> tel
{'jack': 4444, 'guido': 1232, 141: 'hola', ('test', 12): 'hola'}
>>> tel[('test', [12])] = 'hola'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> myTuple = 12, 144, 'hello'
>>> x, y, z = myTuple
>>> x
12
>>> y
144
>>> z
'hello'
>>> tel
{'jack': 4444, 'guido': 1232, 141: 'hola', ('test', 12): 'hola'}
>>> for key, value in tel.items():
...   print(key, value)
... 
jack 4444
guido 1232
141 hola
('test', 12) hola
>>> tel.items()
dict_items([('jack', 4444), ('guido', 1232), (141, 'hola'), (('test', 12), 'hola')])
>>> for key, value in tel.items():
...   print(key)
... 
jack
guido
141
('test', 12)
>>> for key, value in tel.items():
...   print(key)
... 
jack
guido
141
('test', 12)
>>> for item in tel.items():
...   print(item)
...   print(item[0], item[1])
...   mykey, myvalue = item
...   print(mykey, myvalue)
... 
('jack', 4444)
jack 4444
jack 4444
('guido', 1232)
guido 1232
guido 1232
(141, 'hola')
141 hola
141 hola
(('test', 12), 'hola')
('test', 12) hola
('test', 12) hola
>>> 