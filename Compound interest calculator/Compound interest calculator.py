#This is a compound interest convertor


principle = 0 #This is a variable
rate = 0      #This is a variable
time = 0     #This is a variable

while True:
    principle = float(input("Enter the principle: ")) #User should enter the principle (float)
    if principle < 0:
        print("Principle can't be less or equal to 0") #this will be printed if principle is less than zero
    else:
        break  # this stops the program from asking the user to enter the principle over and over again

while True:
    rate = float(input("Enter the interest rate: ")) #User should enter the rate (float)
    if rate < 0:
        print("interest rate can't be less or equal to 0")#this will be printed if rate is less than zero
    else:
        break #this stops the program from asking the user to enter the rate over and over again

while True:
    time = int(input("Enter the time in years: ")) #User should enter the years (integers)
    if time < 0:
        print("time can't be less or equal to 0") #this will be printed if time is less than zero
    else:
        break #this stops the program from asking the user to enter the time over and over again


total = principle * pow((1 + rate / 100), time) # This is the formular for calculating Total after the principle, time and rate
print(f"Your balance after {time} year/s is ${total:.2f}") #This prints your total in two decimal places, after the time
