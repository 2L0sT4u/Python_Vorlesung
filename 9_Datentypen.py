# 27.03.24

## Einfache Datentypen

type(1)
# ->
# int

import sys
sys.maxsize
# ->
# 92233..07

# == 2^63 - 1 ~ 9e18

# float
0.1 + 0.1 + 0.1 == 0.3
# ->
# False

# ~ == 0.30..04

# komplexe Zahl
3 + 6j

c1 = 3 + 6j
c2 = 45 + 9j

c1.real
# ->
# 3

c2.imag
# ->
# 9

c1 + c2
# ->
# 48 + 15j

import math

math.sqrt(9)
# ->
# 3

math.sqrt(-9) # Fehler

import cmath

cmath.sqrt(-9)
# ->
# 3i

# gibt auch decimal statt float

# None

print(None) #nischts halt
# ->
# None

#print() returned None

res = print('abc')

res is None
# ->
# True

# bool

bool(0)
# ->
# False

# bool(a) a!=0 -> True
# jedes Objekt lässt sich durch bool in True oder False umwandeln

bool([])
# ->
# False

bool([None])
# ->
# True


# kollegah hat string und so vergessen