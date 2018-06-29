""" Question 4 """
def k_largest_elements(lst,k):
    lst.sort()
    index = len(lst) - k
    return lst[index:]

if __name__=="__main__":
    print(k_largest_elements([3,9,2,7,1,7,1,3], 4))
