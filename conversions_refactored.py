import re



def convert(fromUnit, toUnit, value=int):
    """ 
    Function to convert any unit (temperature, miles, yards, and meters) into another and returns as a float.
    fromUnit is a str = unit you are converting from
     toUnit is a str = unit you are converting to
     value = value of fromUnit you are converting from"""

    # temperature Kelvin Regex search
    kelvin_Regex = re.compile(r'k|kelvin(s)?', re.I)
    # temperature Fahrenheit Regex search
    fahrenheit_Regex = re.compile(r'f|fahrenheit', re.I)
    # temperature Celsius Regex search
    celsius_Regex = re.compile(r'c|celsius', re.I)
    # distance mile Regex search
    mile_Regex = re.compile(r'mi|mile(s)?', re.I)
    # distance yard Regex search
    yard_Regex = re.compile(r'yd|yard(s)?', re.I)
    # distance meter Regex search
    meter_Regex = re.compile(r'm|meter(s)?', re.I)

    # create custom ConversionNotPossible exception for when incompatible units are entered for conversion
    class ConversionNotPossibleException(Exception):
        pass


    # determine if fromUnit is temperature or distance and perform appropriate conversion
    # start of temperature conversions
    if kelvin_Regex.search(fromUnit):  # determine if fromUnit is Kelvin
        from_kelvin = value - 273.15  # formula to convert to celsius
        if celsius_Regex.search(toUnit):
            result = format(from_kelvin, '.2f')  # set precision to 2 decimal places for celsius conversion
            result_int = float(result)  # store result as an integer
            return result_int
        elif fahrenheit_Regex.search(toUnit):
            result = format(from_kelvin * 9/5 + 32, '.2f')  # complete fahrenheit conversion and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif kelvin_Regex.search(toUnit):
            result = format(value, '.2f')  # return the same value and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        else:
            raise ConversionNotPossibleException('Incompatible units entered for conversion. Enter compatible units and run conversion again.')
    elif fahrenheit_Regex.search(fromUnit):  # determine if fromUnit is Fahrenheit
        from_fahrenheit = (value - 32) * 5/9  # formula to convert to celsius
        if celsius_Regex.search(toUnit):
            result = format(from_fahrenheit, '.2f')  # set precision to 2 decimal places for celsius conversion
            result_int = float(result)  # store result as an integer
            return result_int
        elif kelvin_Regex.search(toUnit):
            result = format(from_fahrenheit + 273.15, '.2f')  # complete kelvin conversion and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif fahrenheit_Regex.search(toUnit):
            result = format(value, '.2f')  # return the same value and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        else:
            raise ConversionNotPossibleException('Incompatible units entered for conversion. Enter compatible units and run conversion again.')
    elif celsius_Regex.search(fromUnit):  # determine if fromUnit is Celsius
        if kelvin_Regex.search(toUnit):
            result = format(value + 273.15, '.2f')  # convert to kelvin and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif fahrenheit_Regex.search(toUnit):
            result = format((value * 9/5) + 32, '.2f')  # convert to fahrenheit and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif celsius_Regex.search(toUnit):
            result = format(value, '.2f')  # return the same value and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        else:
            raise ConversionNotPossibleException('Incompatible units entered for conversion. Enter compatible units and run conversion again.')
        # start of distance conversions
    elif mile_Regex.search(fromUnit):  # determine if fromUnit is Miles
        if yard_Regex.search(toUnit):
            result = format(value * 1760, '.2f')  # convert to yard and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif mile_Regex.search(toUnit):
            result = format(value, '.2f')  # return the same value and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif meter_Regex.search(toUnit):
            result = format(value * 1609.344, '.2f')  # convert to meter and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        else:
            raise ConversionNotPossibleException('Incompatible units entered for conversion. Enter compatible units and run conversion again.')
    elif yard_Regex.search(fromUnit):  # determine if fromUnit is Yards
        if mile_Regex.search(toUnit):
            result = format(value / 1760, '.3f')  # convert to mile and set precision to 3 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif meter_Regex.search(toUnit):
            result = format(value / 1.094, '.2f')  # convert to meter and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif yard_Regex.search(toUnit):
            result = format(value, '.2f')  # return the same value and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        else:
            raise ConversionNotPossibleException('Incompatible units entered for conversion. Enter compatible units and run conversion again.')
    elif meter_Regex.search(fromUnit):  # determine if fromUnit is Meters
        if mile_Regex.search(toUnit):
            result = format(value / 1609.344, '.3f')  # convert to mile and set precision to 3 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif yard_Regex.search(toUnit):
            result = format(value * 1.094, '.2f')  # convert to yard and set precision to 3 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        elif meter_Regex.search(toUnit):
            result = format(value, '.2f')  # return the same value and set precision to 2 decimal places
            result_int = float(result)  # store result as an integer
            return result_int
        else:
            raise ConversionNotPossibleException('Incompatible units entered for conversion. Enter compatible units and run conversion again.')





if __name__ == '__main__':
    fromUnit = input('Enter unit converting from: ')  # request unit to convert from
    toUnit = input('Enter a unit to convert to: ')  # request unit to convert to
    num = input('Enter the value of the unit converting from: ')  # request value to convert
    value = int(num)  # store value as an integer
    result = convert(fromUnit, toUnit, value)  # call function to perform conversion
    print(result)




