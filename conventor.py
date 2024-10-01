

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return(fahrenheit - 32) * 5/9 +32

def convert_temprature():
    return (kelvin - 273.15) * 9/5 + 32

def convert_temprature():
    print("Temprature Unit Converter")
    print("1) Celsius to fahrenheit")
    print("2) fahrenheit to Celsius")
    print("3) Celsius to kelvin")
    print("4) Kelvin to Celsius")
    print("5) Fahrenheit to kelvin")
    print("6) Kelvin to fahrenheit")

    choice = int(input("\inchoose a conversion (1-6): "))