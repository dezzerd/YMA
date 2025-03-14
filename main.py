print('----------------')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += abs(a)
    return result if b >= 0 else -result

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    
    result = 0
    abs_a = abs(a)
    abs_b = abs(b)
    
    while abs_a >= abs_b:
        abs_a -= abs_b
        result += 1
    
    return result if (a >= 0) == (b >= 0) else -result

def calculator():
    print("YMA represent")
    print("Введите 'exit' для выхода")
    
    while True:
        operation = input("Введите операцию (+, -, *, /): ")
        
        if operation.lower() == 'exit':
            break
        
        if operation in ('+', '-', '*', '/'):
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            
            if operation == '+':
                print(f"Результат: {add(num1, num2)}")
            elif operation == '-':
                print(f"Результат: {subtract(num1, num2)}")
            elif operation == '*':
                print(f"Результат: {multiply(num1, num2)}")
            elif operation == '/':
                print(f"Результат: {divide(num1, num2)}")
        else:
            print("Неверная операция. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    calculator()