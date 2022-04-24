'''
Created on Apr 24, 2022
The Objective of this project is to program a game of rock, paper, scissors 
to be played against a computer
@author: Brett Destache
'''

#impot random
import random
#make a boolean variable called keep playing to track weather they want to keep 
#playing and set it to true
kp="true"
#loop one: make a game loop that continues while the keep playing is true print 
#out a statement to welcome the user to the game
while kp=="true":
    print( "Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit")
    
#make variables called userscore and cpuscore to track score set to 0
    userscore=0
    cpuscore=0
#loop two: make a round loop that continues while the userscore and cpuscore is 
#less then 2
    while (userscore<2 and cpuscore<2):
#use input() to get a choice from the user rock paper or Scissors store as a 
#varible. use .lower() to make the userscore choice all lower case
        userchoice=input("choose rock, paper, scissors or q.")
        x= userchoice.lower()
#make a list of the choices then use random.choice to get a random choice for
#the Cpu. store the choice in a variable
        l=("rock","paper","scissors")
        CPUC= random.choice(l)
#make a if/elif/else atatement to check if the user inputs against the cpu's 
#choice  NOTE: you will have tyo compare the user's choice and the cpu's choice 
#to "rock", "paper", and "scissors" separately and combine them with logical 
#operators   
#if the user won, add one to the user score, print out the scores 
#"user [#], cpu[#]"
        if((x=="rock" and CPUC=="scissors")or(x=="paper"and CPUC=="rock")or(x=="scissors"and CPUC=="paper")):
            userscore= userscore +1
            print("user [" +str(userscore)+ "] CPU [" +str(cpuscore)+"]")
#else if (elif) the computer won add one to the computer score and then print 
#the scores
        elif((x=="scissors" and CPUC=="rock")or(x=="rock"and CPUC=="paper")or(x=="paper"and CPUC=="scissors")):
            cpuscore= cpuscore +1
            print("user [" +str(userscore)+ "] CPU [" +str(cpuscore)+"]")
#else if it is a draw print "Draw" then print the scores
        elif((x=="scissors" and CPUC=="scissors")or(x=="rock"and CPUC=="rock")or(x=="paper"and CPUC=="paper")):
            print("Draw")
            print("user [" +str(userscore)+ "] CPU [" +str(cpuscore)+"]")
#else if the user entered "q" then end the round and the game loop use the 
#break statement to end the round. make keep playing False
        elif x=="q": break
#else the user didn't enter acepted input, print "not an option, try again"
        else: print("Not an option,try again")
#print out the thank you message print out who won 
#if the user score is 2, then the user won
        if userscore>=2: print("you won, thanks for playing"
                               " (user [" +str(userscore)+ "] CPU [" +str(cpuscore)+"])")
#elif the cpu score is 2, then the cpu won
        elif cpuscore>=2: print("CPU won, thanks for playing"
                                 " (user [" +str(userscore)+ "] CPU [" +str(cpuscore)+"])")
#print out the final scores