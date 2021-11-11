#Distance Converter App

distance = int(input("Input the distance travelled:"))
unit = input("Input type i.e K for Kms or M for miles:")

if unit.upper()=="K":
    Converted = distance/1.609
    print(f"You have covered {Converted} miles")
elif unit.upper()=="M":
    Converted = distance * 1.609
    print(f"You have covered {Converted} Kms")
else:
    print("Wrong input")
