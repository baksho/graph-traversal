"""
This program demonstrates Breadth First Search (BFS) traversal on a graph represented using adjacency list. The graph structure is given
as input and the BFS traversal is performed starting from a given vertex.
"""
from collections import defaultdict

# class to represent a graph using adjacency list
class Graph:
    def __init__(self): # initialization method
        self.adjList = defaultdict(list)

	# Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)

	# Function to perform Breadth First Search on a graph represented using adjacency list
    def bfs(self, startNode):
        # Create a queue for BFS
        visited = [] # list for visited nodes
        queue = [] # initialize an empty queue
        
        # Mark the current node as visited and enqueue it
        visited.append(startNode) # add the starting node to the visited list
        queue.append(startNode) # add the starting node to the queue
        
        # Iterate over the queue while it's non-empty
        while queue:
            # Dequeue a vertex from queue and print it
            currentNode = queue.pop(0) # pop the first (0-th) element
            print(currentNode, end=" ")
            
            # Get all adjacent vertices of the dequeued vertex currentNode
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.adjList[currentNode]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

# Create a graph
graph = Graph()

# Add edges to the graph
graph.addEdge(5, 3)
graph.addEdge(5, 7)
graph.addEdge(3, 2)
graph.addEdge(3, 4)
graph.addEdge(4, 8)

# print("Graph structure given as input: ")
# print(graph.adjList.keys(), graph.adjList.values())

startNode = 5
# Perform BFS traversal starting from vertex 0
print(f"Breadth First Traversal starting from vertex {startNode}:", end=" ")
graph.bfs(startNode)