# utils.py

import random

def rand_list(list):
    random.shuffle(list)

    return list

def list_of_rand_lists(list,n=1):
    list_of_lists = []
    for i in range(n):
        r_list = rand_list(list)
        list_of_lists.append(r_list)
    
    return list_of_lists

def make_25_element_list(list):
    list_25 = []
    for i in range(25):
        if i==12:
            list_25.append("FREE SPACE")
        elif i<len(list):
            list_25.append(list[i])
        elif len(list)<i<2*len(list):
            j = i - len(list)
            list_25.append(list[j])
        else:
            mult = i//len(list)
            ind = i - mult*len(list)
            list_25.append(list[ind])
    
    return list_25
