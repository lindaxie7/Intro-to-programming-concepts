def DetermineCholesterolRatio(total, hdl):
 ratio = float(total/hdl)

 if ratio <= 3.5:
     return str(ratio) +": less than average risk"
 else:
      if 3.5 < ratio <= 4.5:
       return str(ratio) +": average risk"
      else:
          if ratio > 4.5:
           return str(ratio) +": high risk"
 return ratio
        



def main():
    total = int(input("Please enter an interger in mg/dL units that represent total cholesterol number: "))
    hdl = int(input("Please enter an interger in mg/dL units that represent HDL cholesterol number: "))
    print(DetermineCholesterolRatio(total, hdl))

main()
    
   


