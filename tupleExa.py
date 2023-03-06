
a = 1000000

if a < 1000:
    print("a is less than 10")
else:
    print("a is more than 10")

#loop
obj = [1, 4, 6, 7, 8, 9]
for i in obj:
    print(i*2)

dummy = 0
for j in range(1,6):
    dummy = dummy + j
    print(j)
print(dummy)


wh = 5

while wh > 1:
    print("reached")
    wh = wh - 1


class Multiplier:
    def __init__(self, a):
        self.a = a

    def multiply(self, b=1):
        print(b * (self.a))

x = Multiplier("Hello")
x.multiply(2)


