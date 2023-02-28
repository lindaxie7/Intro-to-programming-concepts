def running_total(mylist):
    newlist = []
    if mylist ==[]:
        return []
   
    i = 0
    sum = 0
    for i in range(0, len(mylist)):
        sum = sum + mylist[i]
        i = i + 1
    newlist.append(sum)
    return newlist
        
def main():
    print(running_total([-1, 2, 3]))

    
main()
