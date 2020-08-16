temperature_Celsius = float(input("Enter temperature: "))
print('Celsius: {}℃'.format(temperature_Celsius))
temperature_Fahrenheit = float(input("Enter temperature: "))
print('Fahrenheit: {}℉'.format(temperature_Fahrenheit))

def main():
    print('Celsius: {}℃ Fahrenheit: {}℉'.format(temperature_Celsius, Celsius_change()))
    print('Fahrenheit: {}℉ Celsius: {}℃'.format(temperature_Fahrenheit,Fahrenheit_change() ))
def Celsius_change():
    temperature_Celsius_change = temperature_Celsius * 9 / 5 + 32
    return temperature_Celsius_change
def Fahrenheit_change():
    temperature_Fahrenheit_change = (temperature_Fahrenheit - 32) * 5 / 9
    return temperature_Fahrenheit_change

main()