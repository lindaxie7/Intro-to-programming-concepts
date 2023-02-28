##myString = input('Please enter a word: ')
##myString = myString.lower()
##print(myString)
##list1 = []
##i = 1
##while
    if myString[0] == myString[i]:
        list1.append(myString)
##
print(list1) 
##    print('\n')


status = True
wordLst = ["Baboon", "racecar"]
while status == True:
    myString = input('Please enter a word: ')
    if myString != '':
        temp = myString
        temp = temp.lower()
        if temp[0] in temp[1:]:
            wordLst.append(myString)
    else:
        print(" ".join(wordLst))
        
        for word in wordLst:
            print(word)
            
        for i in range(len(wordLst)):
            print(wordLst[i])
            
        status = False
  
