# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:06:44 2022
recusiveBottlesOfBeer.py
@author: jgoudy

James Goudy

Text To Speach
https://pypi.org/project/pyttsx3/

Do not use PIP witih ANACONDA
choose pyttsx3 via the Anaconda Navigator

"""

import pyttsx3

# global variables
se = pyttsx3.init()
n = 1

# set the number of bottles
def numBottles():

    global n
    
    try:
        
        n = int(input("Enter the number of bottles"))
    
    except:
        n = 3

# text to speech
def sayBottles(numBottles):
    
    cntr = numBottles
    
    while cntr > 0:
        
        se.say(str(cntr) + " bottles of beer on the wall " +str(cntr) + \
              " bottles of beer. Take one down pass it around " + \
                  str(cntr-1) + " bottles of beer on the wall")
        se.runAndWait()
        cntr -=1


# print the number of bottles using a loop
def bottleloop(numBottles):
    
    cntr = numBottles
    
    while cntr > 0:
        
        print(str(cntr) + " bottles of beer on the wall " +str(cntr) + \
              " bottles of beer. Take one down pass it around " + \
                  str(cntr-1) + " bottles of beer on the wall")
        cntr -=1

# print the number of bottles usinga recursive loop
def bottlerecursive(numBottles):
    
    # base case - base case is the condition that stops the loop 
    if numBottles < 1:
        return
    
    print(str(numBottles) + " bottles of beer on the wall " + \
          str(numBottles) + \
              " bottles of beer. Take one down pass it around " + \
              str(numBottles-1) + " bottles of beer on the wall")
  
    bottlerecursive(numBottles-1)

# play the voices and changle thevoice
def playVoices():
    
    vchoice = 0
    
    # get the voices and store them in a list
    v = se.getProperty('voices')
    
    # print the voices info
    print(v)
    
    # setProperty is used to change the voice
    for i in range(len(v)):
        se.setProperty("voice", v[i].id)
        
        se.say("This is voice " + str(i))
        se.runAndWait()
        
    vchoice = int(input("Please choose a voice"))

    se.setProperty("voice", v[vchoice].id)    

# menu system
def menu():
    
    choice = 0
    
    menuString =    "\n\n1. loop version of Bottles of Beer\n" + \
                    "2. Recursive version of Bottles of Beer\n" + \
                    "3. Spoken version of Bottles of Beer\n" + \
                    "4. Change voice\n" + \
                    "5. Cancel\n"
                    
    print(menuString)
                    
    choice = int(input("Please choose 1,2,3,4,5 : "))
    
    if(choice == 1):
        
        numBottles()
        bottleloop(n)
        
    elif(choice == 2):
        
        numBottles()
        bottlerecursive(n)
    
    elif(choice == 3):
        
        numBottles()
        sayBottles(n)
        
    elif(choice == 4):
        
        playVoices()
    
    else:
        
        return
        

def main():
    
    quit = "n"
    
    while quit != "y":
    
        # note that a try statement will not tell you 
        # where you have a problem.  To be granular, you would
        # need place the  try statment within the individual functions
        try:
            
            menu()
            
            quit = input("Would you like to quit? y/n ").lower()
    
        except:
            
            print("There was an error try again")

    # notify the user the program is doone
    print("\nbye bye")


main()
