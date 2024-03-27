# 27.03.24
##Entscheidungen

a = 5
b = 6

a < b 
# -> 
# true

a > b
# ->
# false

if a < b:
    print('kleiner')
# ->
# kleiner

# wenn wahr ...
    
elif a == b:
    print('gleich')
else:
    print('größer')

# elif -> else if; (wenn nicht wahr,) dann ... wenn ...
# else; (wenn nicht wahr,) dann ...    

res = 10 if a==b else 100
# ==
if a == b:
    res = 10
else:
    res = 100
print(res)
# ==
print(10 if a==b else 100)
# ->
# 100

low = 0
high = 100
value = 50
low <= value <= high
# ->
# true

(low <= value) and (value <= high)
# ->
# true

True and True
# ->
# true
True and False
# ->
# false
False and True
# ->
# false
False and False
# ->
# false

True or True
# ->
# true
True or False
# ->
# true
False or True
# ->
# true
False or False
# ->
# false

1 == 1
# ->
# true

1 != 2
# ->
# true

x = 1
y = 1

x == y # Wert Vergleich (das gleiche)
# ->
# true

x is y # Identität Vergleich (das selbe)
# ->
# false

x is not y
# ->
# true

y = x
print(x is y) 
# -> 
# true

not True
# ->
# false

not not True
# ->
# true

eingabe = input('Eingabe: ') # Eingabe in Terminal
print(eingabe)
# ->
# Eingabe: [123]
# 123

print(eingabe * 2) # eingabe ist String
# ->
# 123123
print(int(eingabe) * 2) # eingabe wird gecasted zu int
# -> 
# 246

# int('1e6') = 1000000 (1 * 10^6)