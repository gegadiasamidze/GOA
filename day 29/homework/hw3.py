fruits = ["Apple", "Banana", "Orange", "Grape", "Mango"]
mixed_list = ["Apple", "Banana", "Car", "Pizza", "Grape", "Pizza", "Mango", "Airplane"]

for item in mixed_list[:]:
    if item not in fruits:
        mixed_list.remove(item)

print(mixed_list)
