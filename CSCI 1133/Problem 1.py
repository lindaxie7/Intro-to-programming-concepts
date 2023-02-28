def cntWordOccur(string_of_sentences, word_to_find):
    string_of_sentences = string_of_sentences.split()
    count = 0
    for var in string_of_sentences:
      
        if (var == word_to_find):
            count = count + 1
    return count

def main():
  string_of_sentences = input("Please enter a string that represents a string of one or more sentences: ")
  word_to_find = input("Please enter a string that represents a word: ")
  print(cntWordOccur(string_of_sentences, word_to_find))


main()




