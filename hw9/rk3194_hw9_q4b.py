""" Question 4b """
def intersection_list(lst1,lst2):
    int_lst = []
    num_dict = {}
    for item in lst1:
        if item not in num_dict.keys():
            num_dict[item] = 0
    for item in lst2:
        if item in num_dict:
            int_lst.append(item)

    return int_lst
