def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

number = int(input("Digite um número: "))
if is_fibonacci(number):
    print(f"{number} pertence à sequência de Fibonacci.")
else:
    print(f"{number} não pertence à sequência de Fibonacci.")
