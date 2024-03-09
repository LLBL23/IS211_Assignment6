
def convert_celsius_to_kelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    # kelvins = 0
    cel_to_kel = float(celsius) + 273.15
    cel_to_kel_result = format(cel_to_kel, '.2f')  # set precision to 2 decimal places
    kelvins = float(cel_to_kel_result)  # convert back to a float

    return kelvins


def convert_celsius_to_fahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    # fahrenheit = 0
    cel_to_fah = (float(celsius) * 9/5) + 32
    cel_to_fah_result = format(cel_to_fah, '.2f')  # set precision to 2 decimal places
    fahrenheit = float(cel_to_fah_result)  # convert back to a float
    
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    fah_to_cel = (fahrenheit - 32) * 5/9
    fah_to_cel_result = format(fah_to_cel, '.2f')  # set precision to 2 decimal places
    celsius = float(fah_to_cel_result)

    return celsius


def convert_fahrenheit_to_kelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    fah_to_kel = (fahrenheit - 32) * 5/9 + 273.15
    fah_to_kel_result = format(fah_to_kel, '.2f')  # set precision to 2 decimal places
    kelvins = float(fah_to_kel_result)

    return kelvins


def convert_kelvin_to_fahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    kel_to_fah = (kelvin - 273.15) * 9/5 + 32
    kel_to_fah_result = format(kel_to_fah, '.2f')  # set precision to 2 decimal places
    fahrenheit = float(kel_to_fah_result)

    return fahrenheit


def convert_kelvin_to_celsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    kel_to_cel = (kelvin - 273.15)
    kel_to_cel_result = format(kel_to_cel, '.2f')  # set precision to 2 decimal places
    kelvin = float(kel_to_cel_result)

    return kelvin



if __name__ == '__main__':
    # request celsius input to convert to kelvin
    to_kel_from_cel = input('Enter a temperature in Celsius to convert to Kelvin: ')
    to_kel_from_cel_int = float(to_kel_from_cel)  # store input as integer
    result = convert_celsius_to_kelvin(to_kel_from_cel_int)  # call function to perform conversion
    print(f' {result} K')

    # request celsius input to convert to fahrenheit
    to_fah_from_cel = input('Enter a temperature in Celsius to convert to Fahrenheit: ')
    to_fah_from_cel_int = float(to_fah_from_cel)  # store input as integer
    result = convert_celsius_to_fahrenheit(to_fah_from_cel_int)  # call function to perform conversion
    print(f' {result} °F')

    # request fahrenheit input to convert to celsius
    to_cel_from_fah = input('Enter a temperature in Fahrenheit to convert to Celsius: ')
    to_cel_from_fah_int = float(to_cel_from_fah)  # store input as integer
    result = convert_fahrenheit_to_celsius(to_cel_from_fah_int)  # call function to perform conversion
    print(f' {result} °C')

    # request fahrenheit input to convert to kelvin
    to_kel_from_fah = input('Enter a temperature in Fahrenheit to convert to Kelvin: ')
    to_kel_from_fah_int = float(to_kel_from_fah)  # store input as integer
    result = convert_fahrenheit_to_kelvin(to_kel_from_fah_int)  # call function to perform conversion
    print(f' {result} K')

    # request kelvin input to convert to fahrenheit
    to_fah_from_kel = input('Enter a temperature in Kelvin to convert to Fahrenheit: ')
    to_fah_from_kel_int = float(to_fah_from_kel)  # store input as integer
    result = convert_kelvin_to_fahrenheit(to_fah_from_kel_int)  # call function to perform conversion
    print(f' {result} °F')

    # request kelvin input to convert to celsius
    to_cel_from_kel = input('Enter a temperature in Kelvin to convert to Celsius: ')
    to_cel_from_kel_int = float(to_cel_from_kel)  # store input as integer
    result = convert_kelvin_to_celsius(to_cel_from_kel_int)  # call function to perform conversion
    print(f' {result} °C')

