def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1/2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")
    else:
        print("Invalid choice!")

def length_converter():
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Inches to Centimeters")
    print("4. Centimeters to Inches")
    choice = input("Choose conversion (1/2/3/4): ")

    if choice == '1':
        meters = float(input("Enter length in meters: "))
        print(f"{meters} meters is {meters / 1000} kilometers")
    elif choice == '2':
        km = float(input("Enter length in kilometers: "))
        print(f"{km} kilometers is {km * 1000} meters")
    elif choice == '3':
        inches = float(input("Enter length in inches: "))
        print(f"{inches} inches is {inches * 2.54} cm")
    elif choice == '4':
        cm = float(input("Enter length in cm: "))
        print(f"{cm} cm is {cm / 2.54} inches")
    else:
        print("Invalid choice!")

def weight_converter():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose conversion (1/2): ")

    if choice == '1':
        kg = float(input("Enter weight in kg: "))
        print(f"{kg} kg is {kg * 2.20462} pounds")
    elif choice == '2':
        lbs = float(input("Enter weight in pounds: "))
        print(f"{lbs} pounds is {lbs / 2.20462} kg")
    else:
        print("Invalid choice!")

while True:
    print("\nUnit Converter")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")
    print("4. Exit")

    choice = input("Choose a category (1/2/3/4): ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    elif choice == '4':
        print("bye")
        break
    else:
        print("Invalid choice! Please try again.")

