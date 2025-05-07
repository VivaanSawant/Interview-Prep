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

