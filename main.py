#1
data = {"Ali": 85, "Vali": 90, "Sami": 78}

sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print(sorted_data)

#2
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1 | dict2   # Python 3.9+

print(merged)
