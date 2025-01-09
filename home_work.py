def summarize(*a):
    return sum(a)

print(summarize(1, 2, 3, 4, 5))

# 2

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

describe_person(name="Жума", age=18, city="Бишкек")
