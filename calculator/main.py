ab = int(input("Enter a first number: "))
bc = int(input("Enter a second number: "))
ee = input("*, /, +, -: ")
if ee == "*":
    print(ab * bc)
elif ee == "/":
    print(ab / bc)
    if bc != 0:
        print("Не возможно деление на ноль")
elif ee == "+":
    print(ab + bc)
elif ee == "-":
    print(ab - bc)
else:
    print("операция неверна")