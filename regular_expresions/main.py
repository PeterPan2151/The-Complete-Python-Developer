import re



string1 = 'search inside of this text, please'
a = re.search('this', string1)
print(a.span())


# Password validation excercise
# 8 char long
# contain any letter, numbers, $%#@
pattern = re.compile(r"^[a-zA-Z0-9$%#@]{8,}\d")
string2 = 'Karenylucy2151'
b = pattern.fullmatch(string2)
print(b)

