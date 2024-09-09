# Prompts the user for mass as an integer (in kilograms)
print("Input the mass in kilograms")
mass = input("m: ")

# Convert the string to integer
m = int(mass)

# Speed of light in m/s
c = 300000000

# Compute for the equivalent number of Joules as an integer
E = m * (c ** 2)

# Print the result
print("E:", E)
