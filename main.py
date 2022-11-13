CorF = int(input("Enter 1 if you want to convert Celsius to Fahrenheit or enter 2 if you want to Convert Fahrenheit to Celsius: "))

if CorF == 1:
    c = float(input("Please enter a value in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}ºC is {f}ºF")