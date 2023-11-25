# Python Program to Convert Celsius To Fahrenheit and vice versa

celc = float(input("Enter the temprature in celcius : "))
frnhte = (celc * (9/5)) + 32
print("Temparature in faranhite is",frnhte,"F")

frnhte = float(input("Enter the temprature in faranhite : "))
celc = (frnhte-32)*(5/9)
print("Temparature in celcius is",celc,"C")