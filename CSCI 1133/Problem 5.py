def ForLoop(mylist):
 ##newlist = []
    count1 = 0
    count2 = 0
    count3 = 0

    for words in mylist:
        if type(words) == int:
            count1 = count1 + 1
         
        elif type(words) == str:
            count2 = count2 + 1
           
        else:
            count3 = count3 + 1
          
    return [count1, count2, count3]

def main():
 ##mylist = input("please enter a list: ")
 print(ForLoop([1, 2, 3, "a", "b", 4]))


main()
             
             
    
