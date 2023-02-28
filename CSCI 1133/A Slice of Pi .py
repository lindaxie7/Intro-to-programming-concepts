import random
import math
def estimatePi(sampleSize):
    hits = 0
    for i in range(sampleSize):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = math.sqrt(x * x + y * y)
        if r <=1:
            hits = hits + 1
    pi = 4 * (hits / sampleSize)
    return pi

def main():
    answer = "y"
    while answer == "y":
        sampleSize = int(input("Enter a sample size to calculate pi:  "))
        pi = estimatePi(sampleSize)
        print(pi)
        answer = input("Do you want to continue (y/n)?  ")

main()
