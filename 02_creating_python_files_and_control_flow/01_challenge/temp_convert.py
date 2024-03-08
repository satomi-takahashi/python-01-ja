def convert():
    temp = float(input("Enter the room temperature:")) #20
    unit = str(input("Enter the unit 'f' for Fahrenheit or 'c' for Celcius:")) # f or c
    converted_temp = 0
    if unit == 'f' : 
        converted_temp = (temp - 32) * 5/9
    elif unit == 'c' :
        converted_temp = (temp * 9/5) + 32
    return converted_temp
    
convert()
