def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(1, 2, 3, 4))  
print(multiply_all(5, 6))        
print(multiply_all())           