name = str(input("Enter Your Name: "))
height = float(input("Put your Height in Meters: "))
weight = float(input("Put your Weight in KG: "))
print("Your body mass index is: ", round(weight / (height * height), 2))