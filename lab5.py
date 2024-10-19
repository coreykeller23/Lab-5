"""
Author:Corey Keller
File Name:lab5.py
Creation Date:2.21.24
Purpose:Given the string, determine if 4 random classes get spellcasting, and if so how many slots they have.
Then calculate the average number of spell slots of the classes that have spellcasting.
"""
import lab5utility
import random
string="Barbarian,No,0;Bard,Yes,22;Cleric,Yes,22;Druid,Yes,22;Fighter,No,0;Monk,No,0;Paladin,Yes,15;Ranger,Yes,15;Rogue,No,0;Sorcerer,Yes,22;Warlock,Yes,5;Wizard,Yes,22"

#create variable of list type to split the string
classes=string.split(";")

#create an empty list to populate
entry=[]
#use a for loop to iterate over the split string into sublists
for item in classes:
    splitItems=item.split(",")
    entry.append(splitItems)

#create a variable to choose 4 indexes
randomClasses=random.sample(entry,4)

#call the two functions to complete the tasks using the variables provided as arguments
lab5utility.randomClassSelect(randomClasses)

lab5utility.spellSlotAvg(entry)
