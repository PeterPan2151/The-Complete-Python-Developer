from translate import Translator

translator = Translator(to_lang='ja')

with open('sample.txt', 'r') as file:
    content = file.read()

translation = translator.translate(content)
print(translation)

