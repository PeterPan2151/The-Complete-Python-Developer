import re

string1 = 'search inside of this text, please'
a = re.search('this', string1)
print(a.span())
