import random

list1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum1 = dice1 + dice2

    list1[sum1-2] += 1

for i in range(len(list1)):
    print("{0:2d}: {1:5d}".format(i+2, list1[i]))

    
