#write a python program to create a python list of your favourite fruits(minimum 5).
# then perform the given operations on it.

fruits=["mango","pineapple", "berry","plum","grapes"]

#length of list
print("Length of fruits list is ",len(fruits))


#adding values to list
fruits.append("berry")

print("Updated list is ", fruits)

#indexing
print("I Like", fruits[5])

#removing values from list
fruits.remove("mango")

print("updated list after removing", fruits)

#sorting
fruits.sort()
print("sorted list is",fruits)

fruits.reverse()
print("Reversed list is", fruits)

#slicing
print("sliced list",fruits[1:3])