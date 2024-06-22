expression = input("Expresion: ").lower().split()
x = float(expression[0])
z = float(expression[2])

if expression[1] == "+":
    print(x + z)
elif expression[1] == "-":
    print(x-z)
elif expression[1] == "/" and z != 0:
    print(x / z)
elif expression[1] == "*":
    print(x * z)
else:
    print("Either Z is 0 while (/) or incorrect expression!")

