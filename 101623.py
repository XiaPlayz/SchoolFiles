fahrenheit = 0
kelvin = 0
kelvin = input("How many kelvin do you want to convert?: ")
kelvin = float(kelvin)
firstProcess = kelvin - 273.15
fahrenheit = firstProcess * 1.8 +32
print(f"{kelvin} kelvin is equal to {fahrenheit:.2f} fahrenheit.")