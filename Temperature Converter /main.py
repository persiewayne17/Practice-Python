def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

while True:
    print("\nSelect conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    try:
        choice = int(input("Enter choice (1/2/3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 3:
        break

    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")
        continue

    if choice == 1:
        converted_temp = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temp:.2f}°F")  # Format to 2 decimal places
    elif choice == 2:
        converted_temp = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temp:.2f}°C")  # Format to 2 decimal places
    else:
        print("Invalid choice.")