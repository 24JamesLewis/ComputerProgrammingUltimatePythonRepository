def count_failing_grades(grades):
    count = 0
    for grade in grades:
        if grade <= 60:
            count = count + 1
    return count

grades1 = [87, 56, 72, 91, 33]
returngrades = count_failing_grades(grades1)
print(returngrades) 

def count_act_scores(scores):
    count1 = 0
    for score in scores:
        if score <= 36 and score >= 1:
            count1 = count1 + 1
    return count1 

act_scores = [20, 56, 1, 0, 36]
return_valid_act = count_act_scores(act_scores)
print(return_valid_act)

def number_sum(number):
    total = 0 
    total = sum(number)
    return total
numbers = [7, 4, 3, 19, 12]
sum_of_numbers = number_sum(numbers)
print(sum_of_numbers)

def average_act_score(scores):
    total1 = 0
    for numbers in scores:
        total1 = total1 + numbers

    return total1 / len(scores)

list = [23, 11, 36, 3]
result = average_act_score(list)
print(result)

def all_true(list):
    for boolean in list:
        if boolean == False:
            return False

    print("hey, I got to line 46")
    

print(all_true(["true", "true", "true"]))
print(all_true(["true", "false", "true"]))

#def any_true(list):
    
#def mostly_true(list):
    

def has_vowel(letters): 

    for letter in letters:
        if letter in "aeiou":
            return True
    return False

print("Demonstrate has_vowel:")
print(has_vowel(["a", "e", "i" ]))
print(has_vowel(["b", "f", "g" ]))
print(has_vowel(["h", "g", "i" ]))

def all_the_same(numbers):
    for number in numbers:
        
        if number: 
            return True
        else:
            return False

print("Demonstrate all_the_same:")        
print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 3]))

#def increasing(list):
   
print("Demonstrate increasing:")

#def is_incrementing():


#def has_adjacent_repeat():


#def sum_with_skips():
   