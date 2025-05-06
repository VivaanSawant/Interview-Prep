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

#operators



