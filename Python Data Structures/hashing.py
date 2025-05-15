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