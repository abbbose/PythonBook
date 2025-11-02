# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 15:31:21 2025

@author: abbos
"""
 #String & String Method   
 #to know data type with type
#1



type("HelloWorld123") #type = str 
#2
phrase = "Hello, World"
type(phrase)


string1 = 'Hello, World'
string2 = "1234"

string3 = "We're #1!"
string4 = 'I said, "Put it over by the lama."'

# text = "She said, "What time is it?"" !syntax error!
text = "She said, \"What time is it?\"" #correct way

#Determine the Length of a String
len(text) 

#Multiple string:
    
long_string = "This multiline string is \
displayed on one line"

paragraph = "Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy.This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time."



wild = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
print( wild[0].lower(), wild[1].lower(), wild[2].lower(), wild[3].lower())

print( wild[0].upper(), wild[1].upper(), wild[2].upper(), wild[3].upper())


string3 = " Cheeseburger "
print("1)rm right space: " + string3.rstrip())
print("2)rm left space: " +  string3.lstrip())
print("3)rm right and left space:" + string3.strip())


string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
print(string1.startswith("be"),
string2.startswith("be"),
string3.startswith("be"),
string4.startswith("be"))









