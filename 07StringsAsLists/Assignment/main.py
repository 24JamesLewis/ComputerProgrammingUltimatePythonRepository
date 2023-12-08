def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False

print("Demonstrate is_alliteration")
print(is_alliteration("When", "Why"))
print(is_alliteration("What", "Snow"))
print(is_alliteration("Hello", "Help"))

def count_vowels(word):
    total = 0
    for letter in word:
        if letter in "aeiou":
         total = total + 1
    
    return total

print("Demonstrate count_vowels")
print(count_vowels("Hello"))
print(count_vowels("Test"))

def count_numbers(numbers):

    total = len(numbers)
    return total

print("Demonstrate count_numbers")
print(count_numbers([1, 3, 5, 7, 8, 2, 4]))

def count_target_letters(word, character):
    total = 0
    target = "a"
    for letter in word:
        if letter == target:
            total = total + 1
    return total

print("Demonstrate count_target_letters")
print(count_target_letters("alphabetical", ""))
    
#def in_alphabetical_order(string):
    #for letter in string:

        
#print(in_alphabetical_order("Test"))
#print(in_alphabetical_order("App"))

#def alternate_case(word):
    #position = [0]
     #for letter in word:
         #if position == :
            #letter.upper(letter)
             #position = position + 2
     #return letter
 
 #print(alternate_case("test")) 

#def remove_vowels(string):
    #for letter in string:
        #if letter == "aeiou" :
            #string = 
    #return string

#print("Demonstrate remove_vowels")
#print(remove_vowels("ate"))

def to_camel_case(string):
    result = ""
    for letter in string:
        if letter != " ":
            result = result + letter
            
    return result

print("Demonstrate camel_case")
print(to_camel_case("hello this is a phrase".title()))

def to_snake_case(string):
    result = ""
    for letter in string:
        if letter != " ":
            result = result + letter
    return result

print("Demonstrate to_snake_case")
print(to_snake_case("hello this is a phrase".replace(" ", "_" )))
#print(to_snake_case("This is a test"))
    
#def without_duplicates(list):

#def filter_valid_act_scores(list):
    
