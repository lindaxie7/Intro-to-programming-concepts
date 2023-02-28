def usingWhileLoop(mylist):


 ##if mylist == []:
   ##newlist = [0, 0, 0]
  ## return newlist
    m = 0
    n = 0
    k = 0
    counter = 0
    while counter < len(mylist):
        if type(mylist[counter]) == int:
            m = m + 1
        elif type(mylist[counter]) == str:
            n = n + 1
        else:
         ##if (type(word) != int and type(word) != str):
            k = k +1
        counter = counter + 1
    newlist = []
    newlist.append(m)
    newlist.append(n)
    newlist.append(k)
    return newlist
             
             
def main():
    ##mylist = input()
    print(usingWhileLoop([1, 2, 3, "a", "b", 4]))
    
main()
