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


def letter_count(list):
    total = 0 
    for letter in list:
        total = total + letter
    pass

print(letter_count)



f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
def most_vowels(words):
    #cur_count = count_vowels(most_vowels(words))
    letters = ""
    #for cur_count in words:
        #if cur_count > count_vowels:
            #pass
        # option1: do an inline loop
        # for letter in words:
        # 
        # option2: define a counting function and use it
        # cur_count = count_vowels(word)

       
    

print(most_vowels(words))

f.close()

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
def average_word_length(words):
    for word in words:
        pass

f = open("../data/gradebook_data.csv", "r" )
reader = csv.reader(f)
count = 0
grade = 0
for row in reader:
    name, gradelevel, percent = row 
    percent = int(percent)
    if percent <= 60 :
        grade = grade + 1


print(grade)

f.close()

f = open("../data/gradebook_data.csv", "r" )
reader = csv.reader(f)
count = 0
grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
freshman = 0
sophmore = 0
junior = 0
senior = 0
for row in reader:
    name, gradelevel, percent = row
    gradelevel = int(gradelevel)
    percent = int(percent)
    if gradelevel == 9:
        freshman = freshman + 1
        grade1 = grade1 + percent
    if gradelevel == 10:
        sophmore = sophmore + 1
        grade2 = grade2 + percent
    if gradelevel == 11:
        junior = junior + 1
        grade3 = grade3 + percent
    if gradelevel == 12:
        senior = senior + 1
        grade4 = grade4 + percent
        

print(freshman, grade1, sophmore, grade2, junior, grade3, senior, grade4)

f.close()

f = open("../data/gradebook_data.csv", "r" )
reader = csv.reader(f)
senior = 0
for row in reader:
    name, gradelevel, percent = row
    gradelevel = int(gradelevel)
    percent = int(percent)
    if percent <= 60 and gradelevel == 12:
        senior = senior + 1
        name 
print(senior, )
