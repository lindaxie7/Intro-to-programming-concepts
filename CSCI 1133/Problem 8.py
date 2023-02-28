def location(mylist, val):
  newlist=[]
  for i in range(len(mylist)-1, -1, -1):
   ## for words in mylist :
    if mylist[i] == val:
      newlist.append(i)
  return newlist

def main():
  print(location([1,2,2,4,4,6,4], 4))

main()
