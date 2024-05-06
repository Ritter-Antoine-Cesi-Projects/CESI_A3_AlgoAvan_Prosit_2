# Importing the necessary libraries
import time
import random
import matplotlib.pyplot as plt

# Function to generate a random graph of n cities
def generate_graph(n):
    # Initializing the graph as an empty list
    graph = []
    # Looping over each city
    for i in range(n):
        # Adding a new list to represent the distances from this city to all others
        graph.append([])
        # Looping over each possible destination
        for j in range(n):
            # If the destination is the same as the current city
            if i == j:
                # The distance is 0
                graph[i].append(0)
            else:
                # Otherwise, generate a random distance between 1 and 100
                graph[i].append(random.randint(1, 100))
    # Return the generated graph
    return graph

# Function to calculate the cost of a path
def path_cost(graph, path):
    # Initializing the cost to 0
    cost = 0
    # Looping over each step in the path
    for i in range(len(path) - 1):
        # Adding the cost of the current step to the total cost
        cost += graph[path[i]][path[i + 1]]
    # Adding the cost to return to the first city
    cost += graph[path[-1]][path[0]]
    # Return the total cost
    return cost

# Function to find the best path
def best_path(graph):
    # Initializing the best path and best cost
    best_path = []
    best_cost = float('inf')
    # Looping over each possible starting city
    for i in range(len(graph)):
        # Creating an initial path with only the starting city
        path = [i]
        # Creating a list of all remaining cities
        cities = list(range(len(graph)))
        # Removing the starting city from the list of remaining cities
        cities.remove(i)
        # Calling the recursive function to find the best path from this city
        best_path, best_cost = best_path_rec(graph, path, cities, best_path, best_cost)
    # Return the best path found
    return best_path

# Recursive function to find the best path
def best_path_rec(graph, path, cities, best_path, best_cost):
    # If all cities have been visited
    if len(cities) == 0:
        # Calculate the cost of the current path
        cost = path_cost(graph, path)
        # If the cost is less than the best cost found so far
        if cost < best_cost:
            # Update the best path and best cost
            best_path = path
            best_cost = cost
    else:
        # Otherwise, for each remaining city
        for city in cities:
            # Create a new path by adding the current city
            new_path = path + [city]
            # Create a new list of cities by removing the current city
            new_cities = cities.copy()
            new_cities.remove(city)
            # Call the function itself with the new path and new list of cities
            best_path, best_cost = best_path_rec(graph, new_path, new_cities, best_path, best_cost)
    # Return the best path and best cost found so far
    return best_path, best_cost

# Lists to store the execution times and the number of cities
execution_times = []
num_cities = []

# Loop to generate graphs of different sizes and measure the execution time
for n in range(2, 10):
    # Generate a graph of n cities
    graph = generate_graph(n)
    # Record the start time
    start_time = time.time()
    # Find the best path
    best_path(graph)
    # Record the end time
    end_time = time.time()
    # Calculate the execution time
    execution_time = end_time - start_time
    # Print the number of cities and the execution time
    print(f"Number of cities: {n}, Execution time: {execution_time} seconds")
    # Add the execution time to the list of execution times
    execution_times.append(execution_time)
    # Add the number of cities to the list of city numbers
    num_cities.append(n)

# Create a plot showing the execution time as a function of the number of cities
plt.plot(num_cities, execution_times)
plt.xlabel('Number of cities')
plt.ylabel('Execution time (seconds)')
plt.title('Execution time of the algorithm by number of cities')
plt.show()