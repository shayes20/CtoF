# Write a print statement with the name of this converter, which is CONVERT CELSIUS TO FAHRENHEIT. Then print a new line
cels = float((input("Write a temperature in Celsius = ")))
fahr = round(((cels * 9 / 5) + 32), 2)
print('Temperature in Fahrenheit = ' + str(fahr) + '°F')
print(str(cels) + '°C' + ' = ' + str(fahr) + '°F')
print('\n')

print("CONVERT FAHRENHEIT TO CELSIUS \n")
# Get the user to input a number of type float - use line 2 for help
cels = round(((fahr - 32) * 5 / 9), 2)
print('Temperature in Celsius = ' + str(cels) + '°C')
print(str(fahr) + '°F' + ' = ' + str(cels) + '°C')
print('\n')

print("CONVERT CELSIUS TO KELVIN \n")
cels = float((input("Write a temperature in Celsius = ")))
# Use the variable kelv and convert it to
kelv = round((cels + 273.15), 2)
print('Temperature in Kelvin = ' + str(kelv) + '°K')
print(str(cels) + '°C' + ' = ' + str(kelv) + '°K')
print('\n')

print("CONVERT KELVIN TO CELSIUS \n")
kelv = float((input("Write a temperature in Kelvin = ")))
cels = round((kelv - 273.15), 2)
print('Temperature in Celsius = ' + str(cels) + '°C')
print(str(kelv) + '°K' + ' = ' + str(cels) + '°C')
print('\n')

print("CONVERT FAHRENHEIT TO KELVIN \n")
fahr = float((input("Write a temperature in Fahrenheit = ")))
kelv = round((((fahr - 32) * 5 / 9) + 273.15), 2)
print('Temperature in Kelvin = ' + str(kelv) + '°C')
print(str(fahr) + '°F' + ' = ' + str(kelv) + '°K')
print('\n')

print("CONVERT KELVIN TO FAHRENHEIT  \n")
kelv = float((input("Write a temperature in Kelvin = ")))
fahr = round((((kelv - 273.15) * (9 / 5)) + 32), 2)
print('Temperature in Fahrenheit = ' + str(fahr) + '°C')
print(str(kelv) + '°K' + ' = ' + str(fahr) + '°F')
print('\n')

print("Thanks for using Temperature Converter")
print("Created by Dev Sharma")
print("Click the run button at the top to use the converted again.")
