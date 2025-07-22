# 1 shopping list manager

# manage a shopping list with add/remove functionality

shopping_list = ["milk", "bread", "eggs"]
shopping_list.append("butter")
shopping_list.remove("bread")
print(shopping_list)
print(f"Shopping List: {shopping_list}") # Shopping List: ['milk', 'eggs', 'butter']

# 2 calculate average of grades

grades = [85, 90, 78, 92]
average = sum(grades) / len(grades)
print(f"Average Grade: {average:.2f}") # Average Grade: 86.25

# 3 filter even numbers
# create a list of even numbers from 1 to 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0] # list comprehension for even numbers
print(f"Even Numbers: {evens}") # Even Numbers: [2, 4, 6, 8, 10]

# 4 remove duplicates
# remove duplicate items from a list

items = ["apple", "banana", "apple", "orange", "banana"]
unique_items = list(dict.fromkeys(items)) # use dict to preserve order and remove duplicates

print(f"Unique Items: {unique_items}") # output: Unique Items: ['apple', 'banana', 'orange']


# 5 matrix transpose
# transpose 2x3 matrix

matrix = [[1, 2, 3], [4, 5, 6]]

transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(f"Transposed Matrix: {transposed}")
# Transposed Matrix: [[1, 4], [2, 5], [3, 6]]