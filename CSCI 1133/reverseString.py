def reverseString(n):
    index = 0
    if len(n) == 1:
      return n
    else:
        return n[-1]+reverseString(n[0:-1])

def main():
    print(reverseString("olleh"))

main()
