from main import Item

item1 = Item("Subhashish", 1000, 2)

# We can't change the name since it is set to readonly mode
item1.name = "Other Item"
# print(item1.read_only_name)

print(item1.name)