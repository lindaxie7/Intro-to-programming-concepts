def two_lists_less_than(list1, list2):
    i = 0
    Stringi = ''
    newlist = []
    for i in range(0, len(list1)):
        temp = list1[i] - list2[i]
        if temp > 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
              
    

def main():
    print(two_lists_less_than([5, 1, 1], [3, 3, 3]))

main()
        
    
