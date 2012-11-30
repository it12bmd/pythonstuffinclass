'''
Created on 01/11/2012

@author: madshintze
'''

def BuyBread():
    print("Buying Bread...")
    return "Bread"

def BuyButter():
    print("Buying Butter...")
    return "Butter"

def BuyJam():
    print("Buying Jam...")
    return "Jam"

Food = []

Food.append( BuyBread() )
Food.append( BuyButter() )
Food.append( BuyJam() )

print(Food) 