some_letters = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set(char for char in some_letters if some_letters.count(char) > 1 ))
print(duplicates)