#  Приведение строк к типу bytes, проверить тип и содержание соответствующих переменных.

word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'
print('\n', word1, type(word1), '\n', word2, type(word2), '\n', word3, type(word3))
b = bytes(word1, 'utf-8')
b2 = bytes(word2, 'utf-8')
b3 = bytes(word3, 'utf-8')
print('\nПосле преобразования:\n', b, type(b), '\n', b2, type(b2), '\n', b3, type(b3))

# Реализовать приведение полученных экземпляров типа bytes к типу str и определить тип,
# содержимое и длину соответствующих переменных.

to_string = str(b, 'utf-8')
to_string2 = str(b2, 'utf-8')
to_string3 = str(b3, 'utf-8')
print('\n Обратно в строку:\n', to_string, type(to_string), '\n', to_string2, type(to_string3),
      '\n', to_string3, type(to_string3))

# Реализовать приведение полученных строк и байтовых последовательностей(используя методы encode и decode)

w1 = 'class'
w2 = 'function'
w3 = 'method'
latin = w1.encode('latin-1')
latin2 = w2.encode('latin-1')
latin3 = w3.encode('latin-1')
print('\n Латиница:\n', latin, type(latin), len(latin), '\n', latin2, type(latin2), len(latin2), '\n', latin3, type(latin3), len(latin3))
back = latin.decode('latin-1')
back2 = latin2.decode('latin-1')
back3 = latin3.decode('latin-1')
print('\n Обратное преобразование:\n', back, type(back), '\n', back2, type(back2), '\n', back3, type(back3))

# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

w1 = b'attribute'
# w2 = b'класс'  невозможно записать
# w3 = b'функция' невозможно записать
w4 = b'type'
print('\n Возможно записать: ', '\n', w1, type(w1), '\n', w4, type(w4), ' \nНевозможно записать: «класс», «функция»,')
