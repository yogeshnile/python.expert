#Author:- @python.expert

#import dependencies
import random

#Store a all word to use in password
word = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+|~[]-=?"

#Set a Password Length
passlen = 12

#Generate a Password
password = "".join(random.sample(word,passlen))

#Print a Password
print(password)