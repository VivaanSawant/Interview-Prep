# REVIEW

class Human:
    def __init__(self, hands):
        self.hands = hands;
    def getHands(self):
        return self.hands
    

Vivaan = Human(4);

print(Vivaan.getHands())


# inner classes


class Student:
    def __init__(self, name, rollNum):
        self.name = name
        self.rollNum = rollNum
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name, self.rollNum)
        self.lap.show()
        
    class Laptop:
        def __init__(self):
            self.brand = "HP";
            self.cpu = 'i5';
            self.ram = 8;
        
        def show(self):
            print(self.brand, self.cpu, self.ram)
        





s1 = Student('Vivaan', 8)
s2 = Student('Anika', 4)

print(s1.name, s1.rollNum)

s1.show()

print(s1.lap.brand)
lap2 = s2.lap;
lap1 = s1.lap;

lap3 = Student.Laptop()
s1.show()
