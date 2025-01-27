names = ["ალექსანდრე", "გიორგი", "მარიამი", "ნატალია", "დავიდი", "თამარი", "მარიამი", "ანა", "ზურა", "დავით"]
filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)
