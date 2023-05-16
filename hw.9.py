class rectangle:
    def __init__(self,x,y,z,q):
        self.__x=x
        self.__y=y
        self.__z=z
        self.__q=q
    
    def show(self):
        print(f'({self.__x},{self.__y}),({self.__z},{self.__q})')

    def getarea(self):
        return (self.__z-self.__x)*(self.__q-self.__y)

    def getheight(self):
        return self.__q-self.__y

    def getwidth(self):
        return self.__z-self.__x
    
    def getperimeter(self):
        h=r1.getheight()
        w=r1.getwidth()
        return 2(h+w)




r1=rectangle(5,5,20,10)
a=r1.getarea()
p=r1.getperimeter()

r1.show()

print(f'\n넓이는 {a}, 둘레는 {p}')





