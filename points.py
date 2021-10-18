import random
class Points:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.points = [self.__generate_point() for i in range(quantity)]
        print(self.points)

    def __getitem__(self, n):
        return self.points[n]
    
    def __len__(self):
        return len(self.points)

    def __str__(self) -> str:
        return str(self.points)

    def __generate_point(self):
        x = random.uniform(0, self.size)
        y = random.uniform(0, self.size)
        return (x,y)