class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append([start, end, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        edge_index, edge_count = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = [i for i in range(self.num_vertices)]
        rank = [0] * self.num_vertices

        while edge_count < self.num_vertices - 1:
            start, end, weight = self.edges[edge_index]
            edge_index += 1
            x = self.find(parent, start)
            y = self.find(parent, end)

            if x != y:
                edge_count += 1
                result.append([start, end, weight])
                self.union(parent, rank, x, y)

        return result

# Example usage:
graph = Graph(4)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

print(graph.kruskal_mst())
