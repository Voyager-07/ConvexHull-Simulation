import random
import math
import matplotlib.pyplot as plt


# Function to check orientation (clockwise, counterclockwise, or colinear)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Colinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

# Function to compute the Convex Hull using Graham's Scan algorithm
def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    # Find the point with the lowest y-coordinate (and leftmost if tied)
    pivot = min(points, key=lambda point: (point[1], point[0]))

    # Sort points based on polar angle from the pivot point
    sorted_points = sorted(points, key=lambda point: (math.atan2(point[1] - pivot[1], point[0] - pivot[0]), point))
    # math.
    hull = [sorted_points[0], sorted_points[1]]

    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])

        # Plot the current state of the Convex Hull
        plt.cla()
        plt.scatter(*zip(*points), marker='.', color='blue', label='Points')
        plt.plot(*zip(*hull + [hull[0]]), color='red', label='Convex Hull')
        plt.scatter(*zip(*[pivot]), marker='o', color='green', label='Pivot')
        plt.legend()
        plt.pause(0.1)

    return hull

# Generate random points
random.seed(1)
points = [(random.randint(0, 80), random.randint(0, 80)) for _ in range(100)]

hand_points = [(2.8548387096774195, 0.4761904761904765), (2.9032258064516125, 1.2337662337662343), (2.8870967741935485, 1.8398268398268403), (2.4999999999999996, 2.5324675324675328), (2.0806451612903225, 3.116883116883117), (2.0806451612903225, 3.116883116883117), (2.032258064516129, 3.766233766233767), (2.064516129032258, 4.155844155844156), (2.0161290322580645, 4.696969696969697), (2.064516129032258, 5.476190476190476), (2.129032258064516, 6.082251082251083), (2.370967741935484, 5.800865800865801), (2.6290322580645165, 4.978354978354979), (2.7258064516129035, 4.588744588744589), (2.9677419354838706, 4.1991341991342), (3.2903225806451615, 3.917748917748918), (3.5967741935483875, 4.696969696969697), (3.9677419354838706, 5.974025974025975), (3.9677419354838706, 5.606060606060606), (3.9193548387096775, 5.367965367965368), (4.193548387096774, 6.536796536796537), (4.403225806451612, 6.450216450216451), (4.516129032258064, 5.822510822510822), (4.548387096774194, 5.367965367965368), (4.516129032258064, 4.134199134199134), (4.548387096774194, 4.545454545454546), (4.564516129032258, 4.891774891774892), (4.564516129032258, 3.5930735930735933), (4.758064516129032, 3.354978354978355), (5.161290322580646, 4.004329004329005), (5.580645161290322, 4.740259740259741), (5.693548387096774, 5.086580086580087), (6.161290322580646, 5.476190476190476), (6.435483870967742, 5.64935064935065), (6.35483870967742, 4.978354978354979), (6.290322580645162, 4.06926406926407), (6.209677419354838, 3.5281385281385287), (6.016129032258064, 2.9653679653679657), (5.338709677419354, 2.1428571428571432), (5.629032258064516, 2.467532467532468), (5.048387096774194, 1.5584415584415587), (4.67741935483871, 1.471861471861472), (4.564516129032258, 1.0173160173160178), (4.483870967741936, 0.6060606060606062), (4.46774193548387, 0.38961038961038996)]

# Initialize the plot
plt.figure()
plt.ion()
plt.show()

# Call the convex_hull function to compute and animate the Convex Hull
convex_hull_points = convex_hull(points)

# Keep the plot window open until manually closed
plt.ioff()
plt.show()

print(convex_hull_points)
# points = []
#
# # Function to handle mouse click events
# def onclick(event):
#     if event.button == 1:  # Left mouse button
#         x, y = event.xdata, event.ydata
#         points.append((x, y))
#         plt.scatter(x, y, c='red')  # Plot a red point at the clicked location
#         plt.draw()
#
# # Create a figure and plot
# fig, ax = plt.subplots()
# ax.set_title('Click on the graph to add points')
# ax.set_xlim(0, 10)  # Adjust the x-axis limits as needed
# ax.set_ylim(0, 10)  # Adjust the y-axis limits as needed
# plt.connect('button_press_event', onclick)  # Connect the click event to the onclick function
#
# # Show the plot and interact with it
# plt.show()
#
# # Display the list of clicked points
# print("Clicked Points:")
# # for point in points:
# #     print(point)
# print (points)
#
