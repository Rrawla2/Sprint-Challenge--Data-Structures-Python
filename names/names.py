import time
import sys
sys.path.append('../binary_search_tree')
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Create a new binary search tree
binary_search = BSTNode("names")
# insert the names from the first file names_1.txt
for name_1 in names_1:
    binary_search.insert(name_1)

# check list 2 for names already in list one - saved in binary_search
# if name_2 is in the tree AND not in the duplicates list
# add name_2 to the duplicates list
for name_2 in names_2:
    if binary_search.contains(name_2) and name_2 not in duplicates:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# original - runtime: 11.969835042953491 seconds - 64 duplicates
# refactor - runtime:  0.26244187355041504 seconds - 64 duplicates


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
