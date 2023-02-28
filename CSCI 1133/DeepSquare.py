def deepSquare(list1):
    ##index = 0
    ##newlist = []
    if list1 == []:
        return []
    else:
        if type(list1[0]) == int:
            ##list1[0] = pow(linst1[0], 2)
            ##newlist.append(list1[0])
            ##index += 1
            return [list1[0] ** 2]+ deepSquare(list1[1:])
        else:
            if type(list1[0]) == list:
                ##if type(list1[index][0]) == int:
                return [deepSquare(list1[0])] + deepSquare(list1[1:])



def main():
    
    
    print(deepSquare([[-1,[2],[3],[[[-4,5]]],[],[]]]))

main()
            
