temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C, F, or K): ").upper()
if unit == 'C':
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"{temperature}°C is equal to {fahrenheit}°F and {kelvin}K.")
elif unit == 'F':
    celsius = (temperature - 32) * 5/9
    kelvin = (temperature + 459.67) * 5/9
    print(f"{temperature}°F is equal to {celsius}°C and {kelvin}K.")
elif unit == 'K':
    celsius = temperature - 273.15
    fahrenheit = (temperature * 9/5) - 459.67
    print(f"{temperature}K is equal to {celsius}°C and {fahrenheit}°F.")
else:
    print("Invalid unit.")
