word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if word1[:len(word2)] == word2:
    print(f'Первое слово "{word1}" начинается с "{word2}".')
else:
    print(f'Первое слово "{word1}" не начинается с "{word2}".')