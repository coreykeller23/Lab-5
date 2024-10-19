"""
Author:Corey Keller
File Name:lab5utility.py
Creation:2.21.24
Purpose:Create functions to use a random selection from the split list and print information, and calculate the average of spell slots among classes that have spellcasting.
"""
#constants for the indexes
CLASS=0
SPELLCASTING=1
SPELLSLOTS=2

#functions for the tasks
def randomClassSelect(randomList):
    for task1 in randomList:
        if task1[1]=="Yes":
            print("{}, {}: {}".format(task1[CLASS],task1[SPELLCASTING],task1[SPELLSLOTS]))
        else:
            print("{}: {}".format(task1[CLASS],task1[SPELLCASTING]))

def spellSlotAvg(entry):
    totalSlots=0
    classAdd=0
    for Class in entry:
        if Class[SPELLCASTING]=="Yes":
            totalSlots=totalSlots+int(Class[SPELLSLOTS])
            classAdd=classAdd+1
    if classAdd>0:
        average=totalSlots/classAdd
        print("The average spell slots among classes that get spellcasting is " + str(float(average)) + ".")
    else:
        print("No spellcasting classes found.")