"""
This program demonstrates Depth First Search (DFS) traversal on a graph represented using adjacency list. The graph structure is given
as input and the DFS traversal is performed starting from a given vertex.
"""
from collections import defaultdict

# class to represent a graph using adjacency list
class Graph:
    def __init__(self): # initialization method
        self.adjList = defaultdict(list)
        self.visited = set() # list for visited nodes
        
	# Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)

	# Function to perform Breadth First Search on a graph represented using adjacency list
    def dfs(self, node):
        # Mark the current node as visited and put it on stack
        self.visited.add(node) # add the starting node to the visited list
        print(node, end=" ") # print the visited node

        # because of the for loop, before it reaches the second child node, it recursively calls the function itself for the first
        # child node - which enables to travel to deep node first, then backtrack to the second node.
        for neighbor in self.adjList[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

# Create a graph
graph = Graph()

# Add edges to the graph
graph.addEdge(5, 3)
graph.addEdge(5, 7)
graph.addEdge(3, 2)
graph.addEdge(3, 4)
graph.addEdge(4, 8)

startNode = 5
# Perform DFS traversal starting from vertex 0
print(f"Depth First Traversal starting from vertex {startNode}:", end=" ")
graph.dfs(startNode)