city_map = {}

cities = ["A", "B", "C"]
city_map["Letters"] = []
city_map["Letters"] += cities

print(city_map.keys())
print(city_map.values())
print(city_map.items())

result = []

for i in city_map.values():
    result.append(i)
    
print(result)

newRes = []

for i in city_map.keys():
    newRes.append(i)
    
print(newRes)

# hash sets

new_set = set()
new_set = {1, 2, 3}
new_set.add(4)
new_set.remove(2)
if 3 in new_set:
    print("Present")
    
    
# no duplicates in this set

print(new_set)

set2 = {6, 7, 8}

print(new_set | set2)
print(new_set & set2)
print(len(new_set))
print(len(set2))


s = set()
print(s)

s.add(1)
s.add(2)
s.add(3)

print(s)

if 1 not in s:
    print(True)
else:
    print(False)
    
string1 = "aaaaaaaaaaabbbbbbbbbbbbbbbbbccccccccccccccccdddddddd"
strSet = set(string1)
print(strSet)

for i in strSet:
    print(i)

newD = {"vivaan": 1, "anika": 2}
print(newD)

newD["udhirna"] = 3
print(newD)

for i in newD:
    print(i)

for i in newD:
    print(newD[i])

if "vivaan" in newD:
    print(True)

if 1 in newD:
    print(True)

if 1 in newD.values():
    print("Its here")

for key, val in newD.items():
    print(f"{key}, {val}")


# heaps and priority queues

