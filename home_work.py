def summarize(*a):
    return sum(a)

print(summarize(1, 2, 3, 4, 5))

# 2

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

describe_person(name="Жума", age=18, city="Бишкек")

# 3
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(1, 2, 3, 4))  
print(multiply_all(5, 6))        
print(multiply_all())           

#4 

def build_profile(name, **kwargs):
    print(f"Имя: {name}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

build_profile("Juma", age=18, city="Bishkek")
