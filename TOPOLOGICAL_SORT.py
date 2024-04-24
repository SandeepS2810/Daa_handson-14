from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.adj_list = defaultdict(list)
        self.V = num_vertices

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(vertex)

    def topological_sort(self):
        visited = [False] * self.V
        result_stack = []
        for vertex in range(self.V):
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, result_stack)
        return result_stack[::-1]

# Example usage:
graph = Graph(6)
graph.add_edge(1, 2)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(3, 5)

print(graph.topological_sort())
