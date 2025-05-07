#functions

def greet():
    print("racist stuff")
    
    
greet()

def fib(x):
    if(x == 0 or x == 1):
        return 1;
    
    return fib(x - 2) + fib(x - 1)

print(fib(5))

vivaan = "vivaan";

def reverse(x):
    return x[-1: -len(x) - 1: -1]

print(reverse(vivaan))

def sum(a, *b):
    c = a;
    for i in b:
        c += i
    return c

print(sum(1, 2, 3))

def factorial(x):
    if(x <= 1):
        return 1
    return x * factorial(x - 1)

print(factorial(4))


# the global keyword makes a variable global


a = 5;
print("asdhfakl", a, "adfas")

l = [1, 2, 3, 4, 5, 6]

def count(l):
    c = 0
    o = 0
    for i in l:
        if(i % 2 == 0): c += 1;
        else: o += 1;
    return c, o


even, odd = count(l)

print(even)
print(odd)



#paiTHOOOn

f = lambda a : a * a
result = f(5)

print(result)

f2 = lambda a, b: a + b
print(f2(4, 5))

def hash(x):
    return 2 * x

def getIndex(hash, x, capacity):
    return hash(x) % capacity

print(getIndex(hash, 5, 3))

l = [1, 2, 3, 4, 5, 6]

def isEven(x):
    if(x % 2 == 0): return True;
    


def filter(filterFunc, lis):
    for i in lis:
        if(not filterFunc(i)): lis.remove(i);
    return lis

l = filter(isEven, l)
print(l)



 # special variables __asldfjasdlf__
 
 

print(__name__) #first moduel name is always main cuz thatst he point of execution

print("hello " + __name__)

if(__name__ == "__main__"):
    print("smth")
    
# allows for modularity

#OBJECT ORIENTED RAHHHHHH

class Computer:
    # include attributes and behavior
    def config(self):
        print("adlkfj")
        
comp = Computer()
comp.config()
Computer.config(comp)

#more objecg shi

# redo

class Human:
    def __init__(self, name, gender):
        self.name = name;
        self.gender = gender;
        
    def config(self):
        print("quicckagaigga")
        
    def printStuff(self):
        print(self.name + ", " + self.gender)
    
    def compare(self, other):
        return len(self.name) > len(other.name)
        
h = Human("Vivaan", "Male")
h2 = Human("Aishah", "Female")
h.printStuff()
h2.printStuff()
h.name = "Varun"
h.printStuff()
h2.printStuff()

print(h.compare(h2))


# instance vs class variables


class Car:
    # defining a variable here beocme sa class variable
    wheels = 4 #belongs to calss namespace
    def __init__(self):
        self.mil = 10 #belongs ot instance namespace
        self.com = "BMW"
    
c1 = Car()
print(c1.wheels)
Car.wheels = 3
print(c1.wheels)

