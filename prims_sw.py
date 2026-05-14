# Prim's Algorithm using User Input
# Starting vertex = 1

n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n + 1):

    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * (n + 1)

visited[1] = True

cost = 0

print("Edge : Weight")

for k in range(n - 1):

    minimum = 999
    x = 0
    y = 0

    for i in range(1, n + 1):

        if visited[i]:

            for j in range(1, n + 1):

                if not visited[j] and graph[i][j]:

                    if graph[i][j] < minimum:

                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])

    cost = cost + graph[x][y]

    visited[y] = True


print("Total Cost =", cost)

