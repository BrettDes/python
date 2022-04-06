'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.
def bollean(b, a):
    if b>2 and a>1:
        print(True)
    else:
        print(False)
    return bollean
b=6
a=2
c= bollean(b,a)
print(c)
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def galloncovert(gallons):
    cups= gallons*16 
    return cups
gallons=1
print(galloncovert(gallons))

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.
def galloncovert(gallonz):
    cups= gallons*16 
    return cups
gallons=1
print(galloncovert(gallons))