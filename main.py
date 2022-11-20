CorF = int(input("Enter 1 if you want to convert Celsius to Fahrenheit or enter 2 if you want to Convert Fahrenheit to Celsius or enter 3 if you want to end: "))

while True:

    if CorF == 1:
        c = float(input("Please enter a value in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}ºC is {f}ºF")

    elif CorF == 2:
        f = float(input("Please enter a value in Fahrenheight: "))
        c = (f - 32) * 5/9
        print(f"{f}ºF is {c}ºC")

    elif CorF == 3:
        break

    else:
        print("ERROR! Make sure you only enter 1, 2, or 3.")