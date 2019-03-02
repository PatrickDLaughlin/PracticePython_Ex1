""" Practice Python Exercise 1
    Patrick Laughlin """

import os
name = input("Please Enter a Name: ")
age = int(input("Please Enter your age: "))
copies = int(input("Please enter number of copies: "))
age = (2019 - age) + 100
i = 0

while i<copies:  
  print("\nYour name is " + name)
  print("You will turn 100 in " + str(age))
  i += 1

os.system("PAUSE")


