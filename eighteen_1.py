class Point: 
    """this is point class"""
    def DistanceFromOrigin(self,x,y):
        """gives distance from origin"""
        x1=x**2
        y1=y**2
        sum1=x1+y1
        return sum1**0.5
    def translate(self,x,y):
            """it gives new point as from method"""
            return f'{x+1},{y+1}'
p=Point()
Y=p.DistanceFromOrigin(1,2)
print(Y)
P=p.translate(1,2)
print(P)


