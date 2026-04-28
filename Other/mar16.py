# # starting to stude mathplotlib
import matplotlib.pyplot as plt
import numpy as np

# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=3)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# plt.tick_params(axis="both", labelsize=14)

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=3)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# plt.tick_params(axis="both", labelsize=14)

# plt.show()


# plt.scatter(2, 4, s=200)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis="both", which="major", labelsize=14)
# plt.show()

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis="both", which="major", labelsize=14)
# plt.show()

# can we connect those points with a line? Yes, we can!
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
plt.plot(x_values, y_values, linewidth=3)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()

# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# # the value of y will be the square of x, so when x is 2, y will be 4, when x is 3, y will be 9, and so on.
# plt.scatter(x_values, y_values, s=40)
# plt.plot(x_values, y_values, linewidth=3)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis="both", which="major", labelsize=14)
# plt.axis([0, 1100, 0, 1100000])
# # what does the axis do? It sets the range of the x and y axes. In this case, we set the x-axis to go from 0 to 1100 and the y-axis to go from 0 to 1,100,000. This allows us to see all the points on the graph without them being too close together or too far apart.
# plt.show()

# red color with squares
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100, c="red", edgecolor="black")

# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis="both", which="major", labelsize=14)
# plt.show()

# x_values = list(range(1, 5001))
# y_values = [x**3 for x in x_values]

# plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Blues, edgecolor="none")
# plt.plot(x_values, y_values, linewidth=3)
# plt.title("Cube Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Cube of Value", fontsize=14)
# plt.tick_params(axis="both", which="major", labelsize=14)
# plt.axis([0, 5100, 0, 130000000000])
# plt.show()

# import matplotlib.pyplot as plt
# from random import choice

# class RandomWalk:
#     """A class to generate random walks."""

#     def __init__(self, num_points=5000):
#         """Initialize attributes of the walk."""
#         self.num_points = num_points

#         # Start at (0, 0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_walk(self):
#         """Generate all points for the walk."""
#         while len(self.x_values) < self.num_points:

#             # Random direction and distance
#             x_step = choice([1, -1]) * choice([0, 1, 2, 3, 4])
#             y_step = choice([1, -1]) * choice([0, 1, 2, 3, 4])

#             # Skip no movement
#             if x_step == 0 and y_step == 0:
#                 continue

#             # Calculate next position
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step

#             self.x_values.append(next_x)
#             self.y_values.append(next_y)


# # Create a random walk instance
# rw = RandomWalk()
# rw.fill_walk()

# # Plot the walk
# plt.scatter(rw.x_values, rw.y_values, s=15, c=rw.y_values, cmap=plt.cm.Blues, edgecolor="none")
# plt.plot(rw.x_values, rw.y_values, linewidth=1)

# # Labels and title
# plt.title("Random Walk", fontsize=24)
# plt.xlabel("X Value", fontsize=14)
# plt.ylabel("Y Value", fontsize=14)
# plt.tick_params(axis="both", which="major", labelsize=14)

# plt.show()
