names = ["Michael", "Sarah", "Jonathan", "Elizabeth", "Alexander", "Emily", "Christopher", "Jessica", "Benjamin", "Charlotte"]
filtered_names = []

for name in names:
    if len(name) <= 10:
        filtered_names.append(name)

print(filtered_names)
