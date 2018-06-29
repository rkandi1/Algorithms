""" Question 4a """
def intersection_list(lst1, lst2):
    lst1.sort()
    lst2.sort()
    new_lst = []
    pointer1 = 0
    pointer2 = 0
    while True:
        if pointer1 >= len(lst1)-1 and pointer2 >= len(lst2)-1:
            if lst1[pointer1] == lst2[pointer2]:
                new_lst.append(lst1[pointer1])
            break
        if lst1[pointer1] == lst2[pointer2]:
            new_lst.append(lst1[pointer1])
            pointer1+=1
            pointer2+=1
        elif lst1[pointer1] > lst2[pointer2]:
            if pointer2 <= len(lst2)-2:
                pointer2+=1
        elif lst1[pointer1] < lst2[pointer2]:
            if pointer1 <= len(lst1)-2:
                pointer1+=1

    return new_lst


if __name__=="__main__":
    print(intersection_list2([3,9,2,7,1,8,22], [4,1,8,2,6,7,45,22]))