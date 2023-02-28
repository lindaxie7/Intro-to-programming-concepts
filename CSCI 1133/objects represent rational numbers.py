class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num 
        if den == 0:
             self.denominator = 1 
        else:
             self.denominator = den
##    def __str__(self): 
##         return str(self.numerator) + '/' + str(self.denominator)
    def __str__(self):
        if self.numerator == 0:
            return str(0)
        else:
            if self.denominator == 1:
                return str(self.umerator)
            else:
                return str(elf.numerator) + '/' + str(self.denominator)
    def scale(self,x):
        self.numerator = x * self.numerator
        self.denominator = x * self.demoniator
num1 = rational(3, 4)

        

