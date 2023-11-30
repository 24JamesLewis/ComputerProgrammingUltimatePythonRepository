def make_abc():
    a = "a"
    b = "b"
    c = "c"
    result = [a, b, c]
    return result
print("Demonstrate make_abc")
print(make_abc())

def equal_edges(number):
    first = number[0]
    second = number[-1]
    if first == second: 
        return True
    else: 
        return False
print("Demonstrate equal_edges")
print("[1, 2, 3, 4, 1] -> ", equal_edges([1, 2, 3, 4, 1]))
print("[5, 6, 7, 8, 9] -> ", equal_edges([5, 6, 7, 8, 9]))
print("[-1, 0, 1, 2, -1] -> ", equal_edges([-1, 0, 1, 2, -1]))
print("[4, 4] -> ", equal_edges([4, 4]))

def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[-1]
    last2 = list2[-1]
    if first2 == last1:
        return True
    else:
        return False
print("Demonstrate common_edge")
print("[1, 2, 3, 4] & [5, 6, 7, 8]-> ", common_edge([1, 2, 3, 4], [5, 6, 7, 8]))
print("[1, 2, 3] & [3, 4, 5]-> ", common_edge([1, 2, 3], [3, 4, 5]))
print("[4, 5, 6] & [7, 8, 9]-> ", common_edge([4, 5, 6], [7, 8, 9]))
print("[-1, 0, 1, 2] & [2, 3, 4, 5]-> ", common_edge([-1, 0, 1, 2], [2, 3, 4, 5]))
print("[3, 3, 3] & [3, 3, 3]-> ", common_edge([3, 3, 3], [3, 3, 3]))

def all_the_same(list):
    first3 = list[0]
    middle = list[1]
    last3 = list[-1]
    if first3 == middle and  first3 == last3:
        return True
    elif middle == first3 and middle == last3:
        return True
    elif last3 == first3 and last3 == middle:
        return True
    else:
        return False
print("Demonstrate all_the_same")
print("[1, 2, 3] -> ", all_the_same([1, 2, 3]))
print("[5, 5, 5] -> ", all_the_same([5, 5, 5]))
print("[-1, 0, 1] -> ", all_the_same([-1, 0, 1]))
print("[3, 3, 3] -> ", all_the_same([3, 3, 3]))
print("[4, 5, 6] -> ", all_the_same([4, 5, 6]))

def all_unique(list):
    first4 = list[0]
    middle1 = list[1]
    last4 = list[-1]
    if first4 != middle1 and first4 != last4:
        return True
    elif middle1 != first4 and middle1 != last4:
        return True
    elif last4 != first4 and last4 != middle1:
        return True
    else:
        return False
print("Demonstrate all_unique")
print("[1, 2, 3] -> ", all_unique([1, 2, 3]))
print("[5, 5, 5] -> ", all_unique([5, 5, 5]))
print("[-1, 0, 1] -> ", all_unique([-1, 0, 1]))
print("[3, 3, 3] -> ", all_unique([3, 3, 3]))
print("[4, 5, 6] -> ", all_unique([4, 5, 6]))

def increasing(list):
    first5 = list[0]
    middle2 = list[1]
    last5 = list[-1]
    if first5 < middle2 < last5:
        return True
    else:
        return False
print("Demonstrate increasing")
print("[1, 2, 3] -> ", all_unique([1, 2, 3]))
print("[5, 5, 5] -> ", all_unique([5, 5, 5]))
print("[-1, 0, 1] -> ", all_unique([-1, 0, 1]))
print("[3, 3, 3] -> ", all_unique([3, 3, 3]))
print("[4, 5, 6] -> ", all_unique([4, 5, 6]))

def all_true(list):
    first6 = list[0]
    middle3 = list[1]
    last6 = list[-1]
    if first6 and middle3 and last6 == True:
        return True
    else:
        return False
print("Demonstrate all_true")
print("[True, False, True] -> ", all_true([True, False, True]))
print("[False, False, False] -> ", all_true([False, False, False]))
print("[True, True, True] -> ", all_true([True, True, True]))
print("[False, True, False] -> ", all_true([False, True, False]))
print("[True, False, False] -> ", all_true([True, False, False]))

def mostly_true(list):
    first7 = list[0]
    middle4 = list[1]
    last7 = list[-1]
    if first7 == True and middle4 == True:
        return True
    elif middle4 == True and last7 == True:
        return True
    elif first7 == True and last7 == True:
        return True
    else:
        return False
print("Demonstrate mostly_true")
print("[True, False, True] -> ", mostly_true([True, False, True]))
print("[False, False, False] -> ", mostly_true([False, False, False]))
print("[True, True, True] -> ", mostly_true([True, True, True]))
print("[False, True, False] -> ", mostly_true([False, True, False]))
print("[True, False, False] -> ", mostly_true([True, False, False]))

def make_copy(list):
   return list
print("Demonstrate make_copy")
original_list = [5, 6, 1]
copied_list = make_copy(original_list) 
print("Original List:", original_list) 
print("Copied List:", copied_list)

def repeat_thrice(integer):
    return integer
print("Demonstrate repeat_thrice")

def make_reversed_copy(list):
    first8 = list[0]
    middle5 = list[1]
    last8 = list[-1]
    if first8 == list[0]:
        return  list[-1]
original_list1 = [1, 2, 3]
print("Demonstrate make_reversed_copy")
print("Original List:", original_list1)
print("Reversed List:", make_reversed_copy(original_list1))

