# Brandon Ching
# CSCI102 - Section C
# Python-TemperatureConverter

input_temp = input()
format = input_temp[len(input_temp)-1]
temp = int(input_temp[0:len(input_temp)-1])

if format == "F":
    temp = round(5 * (temp - 32)/ 9)
    print(f"{input_temp} = {temp}C")
elif format == "C":
    temp = round((9 * (temp)/ 5)+ 32)
    print(f"{input_temp} = {temp}F")
else:
    print("Wrong input format.")
