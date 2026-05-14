

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex name: ")

    neighbors = input("Enter neighbors separated by space: ").split()
        #split() converts the string into a list 

    graph[vertex] = neighbors

visited = set()

# DFS Recursive
def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for i in graph[node]:
            dfs(i)

# BFS
def bfs(start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

start = input("Enter starting vertex: ")

print("DFS Traversal:")
dfs(start)

print("\nBFS Traversal:")
bfs(start)
