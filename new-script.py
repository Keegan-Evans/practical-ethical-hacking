#!/usr/bin/python3

import sys #system functions and parameters
from datetime import datetime as dt #import with alias


#to exit sys we can do:
# sys.exit()
print(dt.now())

my_name  = "keegan"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "this is a sentence"
print(sentence[:4])

print(sentence.split(" "))

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)

print(sentence_split, "\n", sentence_join)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                  hello      "
print(too_much_space.strip())

print("a" in "apple")
letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("Myfavorite move is {}.".format(movie))
