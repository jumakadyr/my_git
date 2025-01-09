def is_substring(s1, s2):
    if s1 in s2:
        return "Подстрока найдена"
    elif s2 in s1:
        return "Подстрока найдена"
    else:
        return "Подстрока не найдена"

s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")

result = is_substring(s1, s2)
print(result)