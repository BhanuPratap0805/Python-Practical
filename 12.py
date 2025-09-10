# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half values in one line and other half in next line
mid = len(t1) // 2
print("First half of tuple:", t1[:mid])
print("Second half of tuple:", t1[mid:])

# b. Tuple with even numbers only
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Tuple with even numbers:", even_tuple)

# c. Concatenate with t2
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# d. Maximum and Minimum value
print("Maximum value in tuple:", max(t3))
print("Minimum value in tuple:", min(t3))
