import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

def count_vowels(word):
    vowel_count = 0
    for letter in word:
        if letter in "aeiou":
            vowel_count = vowel_count + 1
    pass

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
def most_vowels(words):
    cur_count = count_vowels(most_vowels(words))
    letters = ""
    for cur_count in words:
        if cur_count > count_vowels:
            return
        # option1: do an inline loop
        # for letter in words:
        # 
        # option2: define a counting function and use it
        # cur_count = count_vowels(word)

       
    

print(most_vowels(words))

f.close()
