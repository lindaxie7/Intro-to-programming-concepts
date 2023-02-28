def flatDeepSquare(list1):
    newlist = []
    index = 0
    n = 1
    if type(list1[index], int):
        n = pow(list1[index],2)
        newlist.append(n)
        index += 1
        return newlist
    elif type(list1[index], list) and list1[index] != []:
        return flatDeepSquare(list1[index][0:])
        if type(list1[index][index1], int):
            index1 = 0
            index1 += 1
            return flatDeepSquare(list1[index][index1])
        elif type(list1[index][index1], list) and list1[index][index1] != []:
            index1 = 0
            index1 += 1
            return flatDeepSquare([list1[[index][index1]]][0:])
def main():
    print(flatDeepSquare([[-1,[2],[3],[[[-4,5]]],[],[]]]))

main()
                       
    
        
