def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False
    
print(is_alliteration("When", "Why"))
print(is_alliteration("What", "Snow"))
print(is_alliteration("Hello", "Help"))

def count_vowels(word):
    total = 0
    for letter in word:
        if letter in "aeiou":
         total = total + 1
    
    return total

print(count_vowels("Hello"))
print(count_vowels("Test"))

def count_numbers(numbers):

    total = len(numbers)
    return total

print(count_numbers([1, 3, 5, 7, 8, 2, 4]))

def count_target_letters(word, character):
    total = 0
    for character in word:
        total = total + character
    
    return total

print(count_target_letters("alphabetical", "a"))
    
def in_alphabetical_order(word):
    start = word[0]
    for letter in word:
        if letter > start:
            return True
        else: 
            return False
        
print(in_alphabetical_order("What"))
print(in_alphabetical_order("App"))

