import math

x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))
z = int(input("Enter z-coordinate: "))

sum_of_squares = 0

for value in [x, y, z]:
    sum_of_squares += value ** 2


magnitude = math.sqrt(sum_of_squares)


print("The magnitude of the vector is:", round(magnitude, 2))

