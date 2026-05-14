# Kruskal's Algorithm

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges and weights:")

for i in range(e):

    u, v, w = map(int, input().split())

    edges.append([u, v, w])

# Sort according to weight
edges.sort(key=lambda x: x[2])

parent = []

for i in range(n):
    parent.append(i)

# Find parent
def find(x):

    while parent[x] != x:
        x = parent[x]

    return x

cost = 0
count = 0

print("Edge : Weight")

for edge in edges:

    u = edge[0]
    v = edge[1]
    w = edge[2]

    p1 = find(u)
    p2 = find(v)

    # No cycle
    if p1 != p2:

        print(u, "-", v, ":", w)

        cost = cost + w

        parent[p1] = p2

        count = count + 1

    if count == n - 1:
        break

print("Total Cost =", cost)
