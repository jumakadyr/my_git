def calculate(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Unsupported operation.'add' or 'multiply'"

print(calculate("add", 1, 2, 3, 4))      
print(calculate("multiply", 1, 2, 3, 4))