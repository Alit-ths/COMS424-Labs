
my_list = [1, 2, 3, 4, 5]


# im gonna use different list methods
my_list.append(6)
print(f"After append: {my_list}")




temp_list = my_list.copy()  

print(f"After clear: {temp_list}")
copy_list = my_list.copy()
print(f"After copy: {copy_list}")



count_of_3 = my_list.count(3)




print(f"Count of 3 in list: {count_of_3}")
my_list.extend([7, 8, 9])
print(f"After extend: {my_list}")
index_of_2 = my_list.index(2)
print(f"Index of 2: {index_of_2}")


my_list.insert(0, 0)


print(f"After insert at position 0: {my_list}")




popped_element = my_list.pop(3)


print(f"After pop at index 3: {my_list}, Popped element: {popped_element}")


my_list.remove(5)

print(f"After remove 5: {my_list}")




my_list.reverse()

print(f"After reverse: {my_list}")


my_list.sort()
print(f"After sort: {my_list}")
