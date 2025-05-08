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

# inheritance

class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 Working")
        
a1 = A()

a1.feature1()
a1.feature2()

class B():
    def __init__(self):
        print("B init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")
    def feature5(self):
        print("feature 5 working")

b1 = B()
b1.feature3()

c1 = C()
c1.feature1()

# init only called if found for C, if not found, goes to B

