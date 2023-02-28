def cntWordsOccur(sentences):
    wordcounts = []
    
    for words in sentences:
        temp = words
        inlist = False
        for j in range(0, len(wordcounts)):
            if temp == wordcounts[j][0]:
                inlist = True
                
        if inlist == False:
            count = 0
            for i in range(0, len(sentences)):
                if sentences[i] == temp:
                    count = count + 1
            wordcounts.append([temp, count])
    return wordcounts


            
def main():
    print(cntWordsOccur(["I", "I", "am", "a", "cat", "dog", "a", "I"]))
 
main()
