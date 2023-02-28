class measure:
	def __init__(self,feet,inches):
 		self.r = feet
		self.i = inches
	def getR(self):
            return self.r

        def setR(self, r):
            self.r = r
            
        def getI(self):
            return self.i

        def setR(self, i):
            self.i = i

x = measure()
print(x)
print(x.getR() + 'feet', x.getI()+ 'inches')
x.r, x.i
        def __str__(self):
            return (x.getR() + str(self.x), x.getI() + str(self.y))


        def __str__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return measure(x,y)


        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return measure(x,y)
        
        def __sub__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return measure(x,y)


m1 = measure()
m2 = measure(4,11)
m3 = measure(6,10)
print(m1)
print(m2+m3)
print(m3-m2) 
