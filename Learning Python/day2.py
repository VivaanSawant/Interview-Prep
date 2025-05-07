
dawg = [1, 2, "acc"]
print(dawg[2])

dawg.append("gayad")
dawg.pop(3)

print(dawg)

dawg.insert(1, 12)

print(dawg)

#review over

tup = (12, dawg, 14)
print(tup)

dawg.pop(len(dawg) - 1)
print(tup)

print(tup.count)

S = {12, 14, 25, 12}

print(S) 
#can't index in a set

name = "Vivaan"

print(id(name))

#converitng types

a = 5.6;
print(int(a))
b = 5;

print(float(b))

print(b < a)
print(b < int(a))

print(int(True))
print(int(False))
print(float(True))
print(float(False))


print(list(range(10)))
print(list(range(1, 10, 2)))

# dictionaries

d = {'vivaan' : "super cool", 'anika': "gaeee"}

print(d)

print(d["vivaan"])
print(d.values())

print(len(d))

print(not (True and False))

print(8 << 2)
print(8 >> 2)
print(int(0x8))
print(bin(0x8))
print(oct(0x8))

from math import sqrt, pow
print(pow(3, 2))
#whats up aliens my name is anvin reddy lets cnotnnue this seriesi in pITON
import math

x = math.sqrt(9)
print(x)
x = math.sqrt(7)
print(x)
print(math.floor(x))
print(math.ceil(x))
print(math.pow(3, 2))
print(math.pi)

print(int(math.pow(3, 2)))

import math as austin

print(austin.pow(3, 2))
print(austin.sqrt(2232))

first = 5
second = 6
first, second = second, first
print(first)

if (False):
    print("hi")
elif (True):
    print("bye")
else:
    print("dafqu is dis cod")
    
i = 1

while (i <= 5):
    print("frick dis languag")
    i += 1

x = ["vivaan", 12, 23, "dfalkdsj"]

for i in x:
    print(i)

y = "vivaan"

for i in y:
    print(i)
    
for i in range(2):
    print(y[i])
    
for i in range(11, 21):
    print(i)
    
for i in range(11, 21, 2):
    print(i)
    
for i in range(20, 0, -1):
    if(i % 5 != 0):
        print(i)
    
for i in range(20, 0, -5):
    print(i)
    
    
candies = 5;

i = 1;
while(i <= candies):
    print("candy")
    i += 1

#use break to break oops

for i in range(1, 101):
    if(i % 3 == 0 or i % 5 == 0):
        continue
    
    print(i)

rev = "vivaan";
print(rev[-1:-len(rev) - 1:-1])

print(rev[0])



print(rev)

print("#", end = "\n\n")
#this makes it so that a new thing inst redone


for i in range(1, 5):
    for j in range(1, 5):
        print("a ", end = "")
    print("\n")


x = 5

for i in range(0, x):
    for j in range(0, x - i):
        print("a ", end = "")
    print("\n")
        

def isPrime(x):
    for i in range(2, x):
        if(x % i == 0): return False;
    return True;

print(isPrime(7))
print(isPrime(8))

nums = [12, 123, 123123, 123, 31, 32, 33, 45]

for nums in nums:
    if(nums % 2 == 0): print(nums);
    



empt = [None] * 5
print(empt)

#good reference for technical interviews


import array as arr

array1 = arr.array('i', [1, 2, 3, 4])
print(array1[1])
array1.reverse()
print(array1[1])


test = [1, 2, 3]
print(test[0])
test.reverse()
print(test[0])

testString = "vivaan"
temp = [None] * len(testString)

for i in range(0, len(testString)):
    temp[i] = testString[i]

temp.reverse();
result = "".join(temp)
print(result)

newArr = arr.array('u', (i for i in temp))

print(newArr)

t = [1, 2, 3, 4, 5]
for i in range(0, len(t)):
    t[i] = t[i] + 5
    
print(t)

a = t

a[0] = 1222

print(t)
print(a)

dimen = [[None] * 5] * 5
print(dimen)

for i in range(0, len(dimen)): 
    for j in range(0, len(dimen)):
        dimen[i][j] = i * j
        
print(dimen)     

oneD = [None for _ in range(3)]
print(oneD)  

twoD = [[None for _ in range(3)]
        for _ in range(3)]

print(twoD)

#matrix implementations

listA = [1, 2, 3, 4]
print(max(listA))