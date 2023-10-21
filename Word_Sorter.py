#Add the names which needs to be sorted
names = []
while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break
    names.append(name)

sorted_names = sorted(names)


print("Sorted Names in Alphabetical Order:")
for name in sorted_names:
    print(name)
