import matplotlib.pyplot as plt
import random

# Define positions
car_position = (1, 1)
destination = (9, 9)

# Randomly generate obstacle
obstacle_position = (random.randint(2, 8), random.randint(2, 8))

# Function to check if obstacle is on the path (simplified check: same line)
def is_obstacle_on_path(car, dest, obs):
    # Check if the obstacle lies between car and destination roughly on the line
    x_range = range(min(car[0], dest[0]), max(car[0], dest[0]) + 1)
    y_range = range(min(car[1], dest[1]), max(car[1], dest[1]) + 1)
    return obs[0] in x_range and obs[1] in y_range

# Plot
plt.figure(figsize=(6, 6))
plt.grid(True)

# Draw the car
plt.plot(car_position[0], car_position[1], 'bo', markersize=10, label='Car')

# Draw the destination
plt.plot(destination[0], destination[1], 'go', markersize=10, label='Destination')

# Draw the obstacle
plt.plot(obstacle_position[0], obstacle_position[1], 'yo', markersize=10, label='Obstacle')

# Draw path
if is_obstacle_on_path(car_position, destination, obstacle_position):
    plt.plot([car_position[0], destination[0]], [car_position[1], destination[1]], 'r-', label='Path (Obstacle Detected)')
else:
    plt.plot([car_position[0], destination[0]], [car_position[1], destination[1]], 'g-', label='Path (Clear)')

plt.legend()
plt.title("Emotionally-Aware AV Path Simulation")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

import matplotlib.pyplot as plt
import heapq

# Grid size and obstacles
grid_size = 10
obstacles = [(3, 3), (3, 4), (3, 5), (5, 5), (6, 5), (7, 5)]

# Start and destination
start = (1, 1)
end = (8, 8)

# Directions for movement (up, down, left, right, and diagonals)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

# A* algorithm to find the path
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, end, obstacles):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_list:
        _, current_g, current = heapq.heappop(open_list)

        if current == end:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size and neighbor not in obstacles:
                tentative_g_score = current_g + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))

    return None  # No path found

# Get the path using A* algorithm
path = a_star(start, end, obstacles)

# Print the path
print("\n--- Vehicle Path from Start to Destination ---")
if path:
    for step in path:
        print(step)
else:
    print("No path found!")

# Plotting the grid with obstacles, start, end, and path,
plt.figure(figsize=(6, 6))

# Plot obstacles in red
obstacle_x, obstacle_y = zip(*obstacles)
plt.scatter(obstacle_x, obstacle_y, c='red', label='Obstacle', s=100, marker='x')

# Plot start point in blue
plt.plot(start[0], start[1], 'bo', markersize=10, label='Start')

# Plot destination point in green
plt.plot(end[0], end[1], 'bs', markersize=10, label='Destination')

# Plot the path in green
if path:
    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, 'go-', linewidth=2, markersize=8, label='Path')

# Setting the grid and plot labels
plt.grid(True)
plt.title("Vehicle Path from Start to Destination (Avoiding Obstacles)")
plt.xlabel("X")
plt.ylabel("Y")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend()
plt.show()
