word1 = input("Введите первую строку: ")
word2 = input("Введите вторую строку: ")

if len(word1) > len(word2):
    print(f"{word1} длиннее.")
elif len(wowrd1) < len(word2):
    print(f"{word2} длиннее.")
else:
    print("Обе строки имеют одинаковую длину.")