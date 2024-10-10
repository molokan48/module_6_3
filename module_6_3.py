class Horse:
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'FRRRRR'

    def Run (self , dx: int):
        self.x_distance += dx
        return self.x_distance

class Eagle:

    def __init__(self):
        super().__init__()
        self.y_distance  = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def Fly (self , dy: int):
        self.y_distance += dy
        return self.y_distance


class Pegasus( Horse , Eagle ):

    def __init__(self):
        self.x_distance = super().__init__()
        self.y_distance = super().__init__()
        self.sound = super().__init__()

    def move(self , dx , dy):
        self.x_distance = super().Run(dx)
        self.y_distance = super().Fly(dy)

    def get_pos(self):
        return (self.x_distance , self.y_distance)

    def voice(self):
        print(Eagle().sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
