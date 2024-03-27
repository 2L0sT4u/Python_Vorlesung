#27.03.24

## for-Schleife
for x in [1, 2, 3]:
    print(x)
#->
# 1
# 2
# 3
    
for c in 'abc':
    print(c)
#->
# a
# b
# c

for x in range(10): # == range(0,10); 0 inklusive, 10 exklusive
    print(x)
#->
# 0 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
    
for x in range(5):
    print(x, end=' ')
# ->
# 0 1 2 3 4 

for x in range(5):
    print(x, end=' ', sep='#')
# ->
# 0#1#2#3#4
    
for x in range(2, 10, 2):
    print(x, end=' ')
# ->
# 2 4 6 8
    
for x in range(10, 2, -1):
    print(x, end=' ')
# ->
# 10 9 8 7 6 5 4 3
    

## while-Schleife

x = 0
while x < 10:
    print(x, end=' ')
    x += 1
# ->
# 0 1 2 3 4 5 6 7 8 9
    
x = 1    
while True:
    print(10)
    x += 1
    if (x==10):
        break
    if (True):
        continue
    
# ->
# Endlosschleife