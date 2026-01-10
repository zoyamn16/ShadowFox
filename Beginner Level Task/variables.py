print("================================================================")
print("1: Create variable pi and check its data type")
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

print("================================================================")

print("2: Attempt to create a variable named 'for'")

# for = 4  # This will cause an error because 'for' is a reserved keyword in Python as 'for'
# Reason: 'for' is used in loops, so it cannot be used as a variable name

# using a valid variable name to avoid error 
for_variable = 4
print("Value of for_variable:", for_variable)

print("================================================================")

print("3: Calculate Simple Interest")
P = 1000
R = 5      
T = 3      

SI = (P * R * T) / 100
print("Simple Interest for 3 years:", SI)
print("================================================================")
