def maxValue(list1):
    ##index = 0
    ##largest = 0
    ##n = len(list1)
    if len(list1) == 1:
        return list1[0]
    else:
        m = list1[0] - maxValue(list1[1:])
        if m > 0:
            return list1[0]
            ##m = maxValue(list1[1:])
            ##return largest
            
        else:
            ##largest = list1[index + 1]
        
            return maxValue(list1[1:])
    

def main():
    print(maxValue([1, 5, 3, 9, 2]))

main()
    
