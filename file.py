"""
Create a Python file named lab_6-3

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a list of 4 colors and store it as a variable.
Use a method to add 3 more colors to the list in a single statement.
Use a different method to add one additional color to the list.
Use a method to insert a new color at index 3.
Use a method to create a copy of the list
Use a method to remove one element from the copy of the list.

"""

# Author: Andrew Tkacs

# Create a list of 4 colors and store it as a variable

colors = ["red", "blue", "green", "yellow"]

# add 3 more colors to the list

colors.extend(["orange", "purple", "pink"])

# add another color to the list

colors.append("brown")

#insert a new color at index 3

colors.insert(3, "black")

# copy the list

colors_copy = colors.copy()

#remove one element from the copy of the list

if len(colors_copy) > 0:
    colors_copy.pop()  # I removed the color using the pop (removes one color in this situation) function.
else:
    print("The copy is empty, so no element was removed.")

# Print the modified list and its copy

print("Original List:", colors)
print("Copied List:", colors_copy)
