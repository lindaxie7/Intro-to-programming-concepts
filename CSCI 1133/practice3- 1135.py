def inSecond(list1, list2):
    newlist = []
    for word1 in list1:
        for word2 in list2:
            if(type(word1) == int and type(word2) == int and word1 == word2):
                newlist.append(word1)
            if (type(word1) == int and type(word2) == str and word1 == word2.split()):
                newlist.append(word1)
    return newlist
           
def main():
    print(inSecond([1, 4, 2], [4]))

main()
            
                
            
                       
