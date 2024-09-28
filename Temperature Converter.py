# Temperature Converter Program
temp=float(input("Enter the temperature: "))
unit=input("Is it in Celcius or Fahrenheit (C or F): ")
if unit=="C":
    temp=round((9*temp)/5+32,1)
    print(f"{temp}°F")
elif unit=="F":
    temp=round((temp-32)*5/9,1)
    print(f"{temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
