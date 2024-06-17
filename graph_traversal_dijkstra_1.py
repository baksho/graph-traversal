"""
This script demonstrates how to calculate the shortest path from a given starting node to all other nodes,
using Dijkstra's algorithm.
"""
import sys
from collections import defaultdict

# class to represent a graph using adjacency matrix
class Graph:
    def __init__(self, vertices): # initialization method
        self.vertices = vertices
        self.adjMatrix = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        
	# Function to add an edge to the graph
    '''
    This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V,
    there needs to be a path from node B to node A with a value V.
    '''
    def addEdge(self, u, v, weight):
        self.adjMatrix[u][v] = weight
        self.adjMatrix[v][u] = weight

    '''
    Function that implements Dijkstra's single source shortest path algorithm for a graph represented using adjacency matrix
    representation.
    '''
    def dijkstra(self, startnode):
        max_value = sys.maxsize
        '''
        Cost to reach starting point S is set to zero. Cost to reach every other node from S is set to ∞.
        '''
        weight = [max_value]*self.vertices # we use maximum value of system instead of infinite weight
        weight[startnode] = 0
        unvisited_graph = [number for number in range(self.vertices)] # initialize list for unvisited vertices, initially contains all
        
        while unvisited_graph:
            currentnode = self.minDistance(weight, unvisited_graph)
            
            # print("---------------------------------------------------")
            # print("Iteration: ", iter_count)
            # print("Unvisited Graph: ", unvisited_graph)
            # print("Weight: ", weight)
            # print("Current Node: ", currentnode)
            
            unvisited_graph.remove(currentnode) # mark the node as visited
            '''
            Update weigh value of the adjacent vertices of the current vertex only if the new weight is smaller than
            the current weight and the vertex in not visited.
            '''
            for neighbor in range(len(self.adjMatrix[currentnode])):
                if self.adjMatrix[currentnode][neighbor] > 0 and neighbor in unvisited_graph:
                    if weight[neighbor] > weight[currentnode] + self.adjMatrix[currentnode][neighbor]:
                        weight[neighbor] = weight[currentnode] + self.adjMatrix[currentnode][neighbor]
            # print("Updated Weight: ", weight)
        self.printSolution(weight)

    '''
    Utility function to find the next vertex with shortest distance from unvisited_graph list
    '''
    def minDistance(self, weight, unvisited_graph):
        min_value = sys.maxsize
        for node, current_weight in enumerate(weight):
            if current_weight < min_value and node in unvisited_graph:
                min_value = current_weight
                min_index = weight.index(min_value)
        return min_index
        
    def printSolution(self, weight):
        print("Vertex \t Distance from Source")
        for node in range(self.vertices):
            print(node, "\t\t", weight[node])
        
        

graph = Graph(5)

'''
graph.adjMatrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
'''
graph.addEdge(0,1,5)
graph.addEdge(1,2,12)
graph.addEdge(1,3,6)
graph.addEdge(1,4,3)
graph.addEdge(2,4,5)
graph.addEdge(3,4,2)

graph.dijkstra(0)