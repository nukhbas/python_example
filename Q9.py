def is_member(x, list_val):
    list_len = len(list_val)
    for i in len(list_len):
        if x == list_val[i]:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
print(is_member(3,list1))