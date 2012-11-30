'''
Created on 27/11/2012

@author: madshintze
'''

myFile = open("ferieplan2013 14.txt")

def getHolidayFromTxt( fileName):
    myFile = open( fileName)

    myFile.readline()
    myFile.readline()
    
    
Description = myFile.readline()
print(Description)
    
DateLine = myFile.readline()
print(DateLine)
    
DateParts = DateLine.split( "-" )
print( DateParts)
    
StartDate = DateParts[0]
StartDate = StartDate.strip().strip("()")
print( StartDate )
    
    