def countGt(mylist):
    list1 = []
    for x in mylist:
        count = 0
        for y in mylist:
            if y > x:
             count = count + 1
        list1.append(count)
    return list1

def main():
    print(countGt([1, 3, 0, 1, 6]))

main()
   
 
          
