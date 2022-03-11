'''
Created on Feb 27, 2022
The Objective of this project is to program a quiz for user on basic high school
trivia.
@author: Brett Destache
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
Score=0
#Ask the user question one. And store the users answer.
x= input("What is the powerhouse of the cell? A) mitochondria B) nucleus C) ribosome")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if x.upper()=="A": print("correct")
else: print("Incorrect, the correct answer is A")
#Ask the user question two. And store the users answer.
y= input("How many states comprise the United States? A) 13 B) 45 C) 50")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if y.upper()=="C": print("correct") 
else: print("Incorrect, the correct answer is C")
#Ask the user question three. And store the users answer.
z= input(" In y = mx + b, what does m stand for? A) slope B) output C) I don't understand math")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if z.upper()=="B": print("correct")
else: print("Incorrect, the correct answer is B")
#Ask the user question four. And store the users answer.
v= input("In English, a person, place or thing is called: A) verb B) adjective C) noun")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if v.upper()=="C": print("correct")
else: print("Incorrect, the correct answer is C")
#Calculate the percentage the user got. And store it in a variable called p
if x.upper()=="A": a=1
else:a=0
if y.upper()=="C": b=1
else:b=0
if z.upper()=="B": c=1
else:c =0
if v.upper()=="C": d=1
else:d=0
S=Score+a+b+c+d
p=S*100/4
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("you got a "+str(S)+'''/4 or a '''+str(p)+"%")