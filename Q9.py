def is_member(x,list_value):
    list_length = len(list_value)
    for i in range(list_length):
        if x==list_value[i]:
            return True
    return False

abc = [1,4,6,9,34]
print(is_member(4,abc))
print(is_member(20,abc))
