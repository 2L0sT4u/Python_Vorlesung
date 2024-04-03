#03.04.2024

##Dictionarys

d = { 'a':100, 'b':200, 'c':300}

d['a']
# ->
# 100

d['a'] = 1_000 # == 1000
d
# =>
# { 'a':1000, 'b':200, 'c':300}

del d['b']
d
# =>
# { 'a':1000, 'c':300}

d['b'] = 200
d
# =>
# { 'a':1000, 'c':300, 'b':200}

{ 'a':1000, 'c':300, 'b':200, 'a':400}
# =>
# { 'a':400, 'c':300, 'b':200}

'a' in d
# =>
# True

300 in d
# =>
# False

# betrachtet nur Schlüssel
# Schlüssel muss hashable sein

d.values()
# =>
# dict_values([400, 300, 200])
d.keys()
# =>
# dict_keys(['a', 'c', 'b'])
d.items()
# =>
# dict_items([('a', 400), ('c', 300), ('b', 200)])

neu = {'a':10, 'x':20}
d1 = d.copy()
d2 = d.copy()

d1.update(neu)
d1
# =>
# { 'a':10, 'c':300, 'b':200, 'x':20}

for k, v in neu.items():
    d2[k] = v
# == dict.update
d2
# =>
# { 'a':10, 'c':300, 'b':200, 'x':20}

# dict.clear() 
# => 
# {}

dx = dict() # == dx = {}

dict.fromkeys('abc')
# =>
# {'a':None, 'b':None, 'c':None}

dict.fromkeys('abc', 42)
# =>
# {'a':42, 'b':42, 'c':42}

dict.fromkeys('abc', [1, 2, 3])
# =>
# {'a':[1, 2, 3], 'b':[1, 2, 3], 'c':[1, 2, 3]}