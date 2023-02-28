def roundFloat():
    weight = float(input("Input a floating-point number "))
    if weight >= 0:
        weight = weight + 0.5
    elif weight < 0:
        weight = weight - 0.5
    return int(weight)
    
  

def main():
    print('The rounded integer is : ',  roundFloat())
    
main()


