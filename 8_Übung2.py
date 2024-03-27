# 27.03.24

# a) Schreiben Sie eine Schleife, die die Quadrate der Zahlen 10 bis 20 ausgibt mit Hilfe von for
# b) Schreiben Sie eine Schleife, mit while, die das Gleiche tut.
# d) Modifizieren Sie Ihre Schleife aus a) so, dass diese nur jede zweite Zahl ausgibt. Nutzen Sie hierfür eine if-Abfrage und continue im Schleifenkörper
# e)

# a)
print('Aufgabe a:')
for i in range(10, 21, 1):
    print(i*i, end=' ')

# b)
print('\n\nAufgabe b:')
i = 10
while i <= 20:
    print(i*i, end=' ')
    i += 1

# d)
print('\n\nAufgabe d:')
for i in range(10, 21, 1):
    if i%2!=0:
        continue
    print(i*i, end=' ')
