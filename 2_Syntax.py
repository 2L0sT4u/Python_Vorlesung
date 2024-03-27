# 27.03.24
### Kommentare

1+1 
# ->
# =2
2+2
# -> 
# =4


#### Einrückungen

for x in [1,2,3]:
    print(x) # 4 Leerzeichen -> 1 Tab
print('Ende')
# ->
# 1
# 2
# 3
# Ende


### Zeilenumbrüche

't1' 't2' 't3'
# ->
# t1t2t3

#hier Zeilenumbruch wichtig
't1'\
't2'\
't3'
# ->
# t1t2t3

#hier Zeilenumbruch egal
( 
    't1'
          't2'
                    't3'
 )
# ->
# t1t2t3

[
    1,
    2,
    3
]
# ==
[1,2,3]


## Groß- und Kleinschreibung

#a
# !=
#A


## Strings

'abc'
# ==
"abc"

'Sie sagte: "Hallo!".'
# ==
"Sie sagte: \"Hallo!\" "
# Backslash '\' hebt Wirkung von nachfolgendem Zeichen auf

s = """Zeile 1
Zeile 2

Zeile 4
"""
# ==
'Zeile 1\nZeile 2\n\nZeile 4' # \n new line
# ->
# Zeile 1
# Zeile 2
# 
# Zeile 4

