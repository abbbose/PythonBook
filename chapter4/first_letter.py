# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov  2 15:51:15 2025

# @author: abbos
# """
#   The script determine the first 
# letter of the user’s input, convert that letter
# to upper-case, and display it back.

ask = "Tell me your password: "
text = input(ask)
flu=text[0].upper()
print("The first letter you entered was:" + flu)



num = input("Enter a number to be doubled: ")
doubled_num = int(num) * 2
print(doubled_num)


# Review Exercises

# 1) a string containing an integer,

#intager
num1 ="4"
dnum= int(num1)*2
print(dnum)

# 2)
#float
num1 ="4"
dnum= float(num1)*2
print(dnum)

# 3. Create a string object and an integer object, then display them sideby-side with a single print statement by using the str() function.

year=int(2006)
text="I was born in "

textout=text+str(year);
print(textout)

num2=float(input("Enter a:"))
num3=float(input("Enter b:"))

sum = num2*num3
print("sum of ", int(num2) , " and " , int(num3) , "is: ", sum)


weight = float(0.2)
animal = "newt"

print(f"{weight} kg is the weight of the {animal}.")




phrase = "the surprise is in here somewhere";
phrase.find("in")



my_story = "I'm telling you the truth; nothing but the truth!"
my_story.replace("the truth", "lies")
# my_story = my_story.replace("the truth", "lies")



# Review Exercises


phrase1 = "a";
phrase1.find("AAA")


phrase2 = "Somebody said something to Samantha.";
phrase2.replace('s', 'x')


phrase3=input("Write your name in the list: ")

list="Alfa, Betta, Gamma, "

fullist= list + phrase3
print(fullist)
find = input("Find your name in the list: ")
print(fullist.find(find))



















