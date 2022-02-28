'''
Created on Feb 27, 2022
The Objective is to make a program that can complete conversions of miles into 
other units of measurement.
@author: Brett Destache
'''

'''#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.'''
miles=input("How many miles are you seeking to convert?")
'''#Convert miles to yards, using the following:
# 1 mile = 1760 yards.'''
yards= int(miles)* 1790 
'''#Store the value in a variable called yards and print it out with a 
#simple statement.'''
print(str(miles)+''' Miles is equal to '''+str(yards)+''' Yards''')

'''#Convert miles to feet, using the following:
# 1 mile = 5280 feet.'''
feet= int(miles)*5280
'''#Store the value in a variable called feet and print it out with a 
#simple statement.'''
print(str(miles)+" Miles is equal to "+str(feet)+" Feet")
'''#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.'''
Inches= int(miles)*63360
'''#Store the value in a variable called inches and print it out with a 
#simple statement.'''
print(str(miles)+" Miles is equal to "+str(Inches)+" Inches")