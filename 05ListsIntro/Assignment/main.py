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
    first = list1[0]
    first = list2[0]
    last = list1[-1]
    last = list2[-1]
    if first == last:
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
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first == middle and  first == last:
        return True
    elif middle == first and middle == last:
        return True
    elif last == first and last == middle:
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
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first != middle and first != last:
        return True
    elif middle != first and middle != last:
        return True
    elif last != first and last != middle:
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
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first < middle < last:
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
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first and middle and last == True:
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
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first == True and middle == True:
        return True
    elif middle == True and last == True:
        return True
    elif first == True and last == True:
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



def repeat_thrice(item):
    
    return item
print("Demonstrate repeat_thrice")



def make_reversed_copy(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    return list

original_list1 = [1, 2, 3]
reversed_list = make_reversed_copy(original_list1)
print("Demonstrate make_reversed_copy")
print("Original List:", original_list1)
print("Reversed List:", reversed_list)


def reverse_in_place(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    return first == list[-1], middle == list[1], last == list[0]
original_list2 = [1, 2, 3]
print("Demonstrate reverse_in_place:")
print("Original: ", original_list2)
print("Reversed: ", )


