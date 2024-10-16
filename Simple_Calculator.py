# Calculator

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def division(a, b):
    return a/b

operation = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': division
}

num1 = int(input("take first number: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Select operation: ")
num2 = int(input("take second number: "))
calculation = operation[operation_symbol]
answer = calculation(num1, num2)
print(f"{num1}{operation_symbol}{num2} = {answer}")



