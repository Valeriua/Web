list_name = [5, 15, 16, 2, 6]
print("Task 1:")
print((max(list_name) - (min(list_name))))
print(" ")
print("Task2:")
print((list_name[2])**(list_name[4]))
print(" ")
dishes = ("dish1", "dish2", "dish3", "dish4")
print("Task3:")
for x in dishes:
    print(x)
print(" ")
print("Task3:")
some_list = ["Black", 48, "White", 22, "Orange"]
some_list.remove("Orange")
del some_list[0]
some_list.pop(1)
new_some_list = []
for i in some_list:
    new_i=((i)/2)
    new_some_list.append(new_i)
print("Result:")
print(new_some_list)

