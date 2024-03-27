# 27.03.24
# a) Schreiben Sie ein Programm, das vom Nutzer die Eingabe einer Zahl verlangt. Vergleichen Sie diese Zahl mit einer Grenzwert und geben Sie aus, ob die Zahl darüber oder darunter liegt, bzw. dem Grenzwert entspricht.
# b) Schreiben Sie ein zweites Programm, das prüft ob der eingegebene Wert innerhalb eines vorgegebenen Bereich liegt. Nutzen Sie dazu (a) boolsche Operatoren und (b) einen einzeiligen Mehrfachvergleich.

# a
value = int(input('Input value: '))
limit = int(input('Input limit: '))

if value == limit:
    print('value == limit')
elif value >= limit:
    print('value >= limit')
else:
    print('value <= limit')


# b
HIGH = 100
LOW = 10

in_limit = LOW <= value and value <= HIGH
print('value', 'is' if in_limit else 'is not', 'between 10 and 100')