def addPos(mylist):
    i = 0
    ##count = 0
    sum = 0
    newlist = []
    for word in mylist:
        if(word > 0):
            newlist.append(word)
        else:
            newlist = [0]
    for i in range(0, len(newlist)):
        sum = sum + newlist[i]
        i = i + 1
    return sum

def main():
    print(addPos([-2, 5, 15]))

main()
            
    
