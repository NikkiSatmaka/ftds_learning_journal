def convert_celsius_kelvin(temperature, method=0):
    """
    convert_celsius_kelvin(temperature, method: 0 | 1)

    Convert temperature from Celsius to Kelvin or Kelvin to Celsius
    
        Parameters
        ----------
        temperature : integer or float
        method : [0 for celsius to kelvin, 1 for kelvin to celsius]
                 0 by default
    """
    try:
        temperature = float(temperature)  # convert the temperature to float

        if method == 0:  # method 0 is to convert from Celsius to Kelvin
            return temperature + 273.15  # return the Kelvin temperature
        elif method == 1:  # method 1 is to convert from Kelvin to Celsius
            return temperature - 273.15  # return the Celsius temperature
        else:
            print("Please input 0 or 1 as the method")  # should never come out
    except ValueError:
        print('Error: Temperature only accepts integer or float')  # error message


def convert_to_fahrenheit(temperature, input_unit='Celsius'):
    """
    convert_to_fahrenheit(temperature, input_unit)

    Convert temperature from Celsius or Kelvin to Fahrenheit
    
        Parameters
        ----------
        temperature : integer or float
        input_unit : ['Celsius', 'Kelvin']
                     'Celsius' by default
    """
    try:
        temperature = float(temperature)  # convert the temperature to float
        input_unit = input_unit.lower()  # lowercase the input_unit

        if input_unit == 'kelvin':  # check if Kelvin
            temperature = convert_celsius_kelvin(temperature, 1)  # convert to Celsius first
        elif input_unit == 'celsius':  # check if Celsius
            pass  # do nothing
        else:
            print("Please input 'Celsius' or 'Kelvin' as input_unit")  # error message

        return temperature * 1.8 + 32  # return the Fahrenheit temperature
    except ValueError:
        print('Error: Temperature only accepts integer or float')  # error message


def convert_from_fahrenheit(temperature, output_unit='Celsius'):
    """
    convert_from_fahrenheit(temperature, output_unit)

    Convert temperature from Fahrenheit to Celsius or Kelvin
    
        Parameters
        ----------
        temperature : integer or float
        output_unit : ['Celsius', 'Kelvin']
                      'Celsius' by default
    """
    try:
        temperature = float(temperature)  # convert the temperature to float
        output_unit = output_unit.lower()  # lowercase the input_unit
        
        celsius = (temperature - 32) / 1.8  # convert to Celsius first

        if output_unit == 'kelvin':  # check if Kelvin
            return convert_celsius_kelvin(celsius, 0)  # return the Kelvin temperature
        elif output_unit == 'celsius':  # check if Celsius
            return celsius  # return the Celsius temperature
        else:
            print("Please input 'Celsius' or 'Kelvin' as output_unit")  # error message

    except ValueError:
        print('Error: Temperature only accepts integer or float')  # error message