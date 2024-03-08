def convert():
    temp = float(input("Enter the room temperature")) #20
    unit = str(input("Enter the unit 'f' for Fahrenheit or 'C' for Celcius")) # f or c
    unit = unit.lower()
    if unit == "f": 
        result = (temp-32) * 5/9
    elif unit == "c":
        result = (c * 1.8) +32
    return temp

convert()
