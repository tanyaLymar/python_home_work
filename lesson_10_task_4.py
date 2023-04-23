"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


words_array = ["разработка", "администрирование", "protocol", "standard"]

byte_array = [word.encode() for word in words_array]

for i, word in enumerate(byte_array):
    print(f"{words_array[i]} = {byte_array}")

decoded_array = [byte_word.decode() for byte_word in byte_array]

for word in decoded_array:
    print(word)
    