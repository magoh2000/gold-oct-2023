"""
Your module description
"""
def unique(number_list=[]):
    unique_list = []
    for i in number_list: #check all the items in the number list
        if i not in unique_list: #if you any item that is NOT already in the list
            unique_list.append(i) #append the item previously found to the list. 
    return unique_list



print(unique([1,1,2,3,5,9,4,5,8,9]))