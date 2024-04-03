# 03.04.2024

print('Übung 1:')
dict = {'name1':'001', 'name2':'002', 'name3':'003'}
print('\n dict')
print('\n', dict['name1'])
print('\n', 'name17' in dict)
print('\n', dict.values)
print('\n', dict.keys)

print('\n\n Übung 2:')
print('\n', dict.get('name27'))
print('\n', dict.setdefault('name27', 0))

print('\n\n Übung 3:')
ndict = dict.copy()
ndict['name99'] = '099'
print('\n', ndict)



print('\n\n Übung 4:')
del dict['name2']
dict.popitem()
print('\n', dict)

print('\n\n Übung 5:')
i = 0
d = {}
while i < 1000:
    i += 1
    if i == 327:
        d[i] = 12345678
        continue
    d[i] = i
print(d)