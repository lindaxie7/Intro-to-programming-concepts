##1)  Imagine that you have been provided with the following lists of students and their respective test scores: 
## names = ['joe', 'tom', 'barb', 'sue','sally']     scores = [11, 22, 14, 17, 10] 
## 
##Write a function named makeDictionary that takes the two lists and returns a dictionary with the names as the key and the scores as the values. Assign the result of makeDictionary to a variable: scoreDict, which will be used in the exercises that follow. 
## 2) Using scoreDict, display barb's score.  (use the Python command-line interface) 
## 3) Add a score of 18 to scoreDict for a student named john.  (use the Python command-line interface) 
## 4) Create and display a sorted list of all the scores in scoreDict.  (use the Python command-line interface) 
## 5) Calculate the average of all the scores in scoreDict.  (use the Python command-line interface) 
## 6) Tom has just dropped the class. Remove him (and his associated score) from scoreDict. (use the Python command-line interface) 
## 
##7) Change sally's score to 15. (use the Python command-line interface) 
## 
##8) Write another function named getScore that takes a name and a dictionary as arguments and returns the score for that name if it is in the dictionary. If the name is
##
##not in the dictionary, print an error message and return -1. Demonstrate your function to one of the TAs.
##

def makeDictionary(names, scores):
    scoreDict = {}
    for x in range(len(names)):
        ##for y in scores:
            ##scoredict = {'x', y}
        scoreDict[names[x]] = scores[x]
    ##scoreDict['tom'] = 22
##    scoreDict['barb'] = 14
##    scoreDict['sue'] = 17
##    scoreDict['sally'] = 10
    return scoreDict

def getScore(names, scoreDict):
    if names in scoreDict:
        return scoreDict[names]
    else:
        return -1
     

def main():
    names = ['joe', 'tom', 'barb', 'sue','sally']
    scores = [11, 22, 14, 17, 10]
    scoreDict = makeDictionary(names, scores)
    print(scoreDict)
    scoreDict['john'] = 18
    print(scoreDict)

    m = list(scoreDict.values())
    m.sort()
    print(m)
    del scoreDict['tom']
    print(scoreDict)
    print(sum(m)/len(m))
    scoreDict['sally'] = 15
    print(scoreDict)
    print(getScore('sally', scoreDict))
    

    
main()
   


