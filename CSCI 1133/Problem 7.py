def location(mylist, val):

    newlist=[]
    for index in range(0, len(mylist)):
        if mylist[index] == val:
            newlist.append(index)
    return newlist

def main():

 print(location([1, 1, 2, 5, 9, 2], 2))


main()
           
