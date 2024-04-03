#03.04.2024

# Übung 1
opnv = {'a', 'b', 'c', 'd', 'e'}
fahrrad = {'b', 'd', 'f', 'h', 'j'}

opnv_und_fahrrad = opnv.intersection(fahrrad)
opnv_ohne_fahrrad = opnv - fahrrad
opnv_oder_fahrrad = opnv.union(fahrrad)
print(opnv_und_fahrrad)
print(opnv_ohne_fahrrad)
print(opnv_oder_fahrrad)

# Übung 2
menge = {'a', 'c', 'e'}
print(menge.issubset(opnv))
print(menge.issubset(fahrrad))

