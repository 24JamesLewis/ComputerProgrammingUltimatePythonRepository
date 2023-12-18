import csv
import os
import json

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
fail = 0
d = 0
c = 0
b = 0
a = 0

for row in reader:
    name, gradelevel, percent = row 
    percent = int(percent)
    if percent <= 59 :
        fail = fail + 1
    if percent <= 69:
        d = d + 1
    if percent <= 79:
        c = c + 1
    if percent >= 80:
        b = b + 1
    if percent >= 90:
        a = a + 1

#percentage number
# A: 90-100%
# B: 80-89%
# C: 70-79%
# D: 60-69%
# F: 0-59%
                
b = b - a       
c = c - (d + fail)        
d = d - fail        
print("The amount of students with each grades are:")
print("A:", a)
print("B:", b)
print("C", c)
print("D:", d)
print("F:", fail)

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
        grade1 = grade1 / freshman  
    if gradelevel == 10:
        sophmore = sophmore + 1
        grade2 = grade2 + percent
        grade2 = grade2 / sophmore 
    if gradelevel == 11:
        junior = junior + 1
        grade3 = grade3 + percent
        grade3 = grade3 / junior
    if gradelevel == 12:
        senior = senior + 1
        grade4 = grade4 + percent
        grade4 = grade4 / senior
grade1 = grade1 * 100
grade2 = grade2 * 100
grade3 = grade3 * 100
grade4 = grade4 * 100

print("Freshman average:", grade1)
print("Sophmore average:", grade2)
print("Junior average:", grade3)
print("Senior average:", grade4)

f.close()

#individual name list 
f = open("../data/gradebook_data.csv", "r" )
reader = csv.reader(f)
senior = 0
for row in reader:
    name, gradelevel, percent = row
    gradelevel = int(gradelevel)
    percent = int(percent)
    if percent <= 60 and gradelevel == 12:
        senior = senior + 1
        print(name)

f.close()

f = open("../data/1000-largest-us-cities.json", "r")
cities = json.load(f)
f.close()

count = 0
name = ""
growth = 0

for city in cities: 
    if city["state"] == "Kansas":
        pass
    if len(city["city"]) >  0:
        name = city

for growth_from_2000_to_2013 in cities:
    if int(city["growth_from_2000_to_2013"]) > growth:
        growth = growth_from_2000_to_2013

print(cities[48]["city"], cities[131]["city"], cities[167]["city"], cities[192]["city"], cities[201]["city"], cities[337]["city"], cities[540]["city"], cities[646]["city"], cities[734]["city"], )
print(len(city["city"]), name)
print(growth)