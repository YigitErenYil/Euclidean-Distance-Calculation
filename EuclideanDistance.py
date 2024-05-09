# Defining the list of points
points = [(1,8), (2,4), (3,7), (9,6)]

# Function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return pow(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2), 0.5)

distances = []

# Calculate distances between all pairs of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Find and print the minimum distance
print(min(distances))