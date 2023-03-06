class DefineLife:
    life = 1

    def __init__(self, a, b):
        self.firstnum = a
        self.secondnum = b

    def flang(self):
        print("one of the aspects of life")

    def summation(self):
        return self.firstnum + self.secondnum + DefineLife.life


obj = DefineLife(2, 3)
obj.flang()
print(obj.summation())
print(obj.life)

obj1 = DefineLife(40, 50)
obj1.flang()
print(obj1.summation())
print(obj1.life)


