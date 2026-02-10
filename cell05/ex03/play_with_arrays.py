array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

for i in array:
    if i > 5:
        new_array.add(i + 2)
print(f"Orginal array: {array}")
print(f"New array : {new_array}")