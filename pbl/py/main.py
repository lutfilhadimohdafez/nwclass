from medieval import MedievalMarket
from cgpacalculator import CGPACalculator
from namemanipulation import NameManipulation
from dataExtractor import DataExtractor

while True:
    print("===========Welcome to Wong Corpo.============")
    print("")
    print("Please choose from the following option")
    print("")
    print("1. CGPA Calculator")
    print("2. Name Manipulation")
    print("3. Data Extractor")
    print("4. Medieval Market")
    print("5. Exit")
    print("")
    InputMain = int(input("Type number to navigate: "))
    try:
        if InputMain == 1:
            CGPACalculator()
        elif InputMain == 2:
            NameManipulation()
        elif InputMain == 3:
            DataExtractor()
        elif InputMain == 4:
            MedievalMarket()
        elif InputMain == 5:
            break
    except:
        print("Wrong Input!")


