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

def number_sum(numbers):
    