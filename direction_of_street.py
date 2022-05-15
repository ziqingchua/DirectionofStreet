"""
Start by getting the street number
If the street number is even, display eastbound
if it is not even, display westbound
finish program
"""


def calculate_street(street):
    print("Divide: ", street / 2)
    print("Modulus: ", street % 2 == 0)
    if (street % 2) == 0:
        print("Eastbound")
    else:
        print("Westbound")