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

