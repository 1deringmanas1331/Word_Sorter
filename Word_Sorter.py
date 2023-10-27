#Add the names which needs to be sorted
names = []
while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break
    names.append(name)

#sort the names in alphabetical order
sorted_names = sorted(names)


print("Sorted Names in Alphabetical Order:")
for name in sorted_names:
    print(name)
