def IteratingLists(mylist):
    newlist = []
    for words in mylist:
        if type(words) == list:
            for worditems in words:
                if type(worditems) == int:
                    newlist.append(worditems)
        else:
            if type(words) == int:
                newlist.append(words)
                
    return newlist

def main():
 ##mylist = input("please enter a list: ")
 print(IteratingLists([1, [2, 3, 6], "cat", "dog", [5, 6, 8, 9]]))

main()


                    
