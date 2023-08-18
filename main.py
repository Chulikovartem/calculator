def сложение(a, b):
    return a + b

def вычитание(a, b):
    return a - b

def умножение(a, b):
    return a * b

def деление(a, b):
    if b == 0:
        print("На 0 делить нельзя!")
        return
    return a / b

def разделитель(пример):
    for i in пример:
        if i in "+-*/":
            index = пример.index(i)
            a = пример[:index]
            s = пример[index]
            b = пример[index+1:]
            return a, s, b

def main():
    пример = input("Введите пример: ") 
    a, s, b = разделитель(пример)
    print(a, s, b)
    

main()
