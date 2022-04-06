'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
def a (b, c): 
    d= b - c
    return d
b=2
c=1
print(a (b, c))
#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.
def e (f): 
    g= f/2*77+10000
    return g
f=2
print(e (f))
#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.
def h (i): 
    if i==k:
        hi="True"
    else: hi="False"
    return hi

i=2
k=2
print(h (i))
#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.
def l (m,n): 
    if m>n:
        o="M is larger"
    if n>m: o="N is larger"
    else: o="They are equal"
    return o
m=2
n=2
print(l (m,n))
#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
def p (q,r): 
        s=q+r
        return s
q="book"
r="shelf"
print(p (q,r))


#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
def t (u,v,w): 
        if u==v or u==w : x="True"
        else: x="False"
        return x
u=3
v=9
w=6
print(t (u,v,w))
#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.
def y():
    z="Brett"
    return z
print(y())


#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.
def aa (ab): 
        if ab=="Green":"That's my favorite color!"
        else:"That is not my favorite color try again."
ab="Green"
print(aa(ab))


#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.
def ad (ae):
        while ae>0:
            print(ae)
            ae-=1
            if ae==0: break
ae=5
print(ad(ae))

