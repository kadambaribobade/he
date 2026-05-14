import heapq
graph = {
    'a': [('b', 4), ('c', 3)],
    'b': [('f', 5), ('e', 12)],
    'c': [('e', 10), ('d', 7)],
    'd': [('e', 2)],
    'e': [('z', 5)],
    'f': [('z', 16)],
    'z': []
}

heuristic = {
    'a': 14,
    'b': 12,
    'c': 11,
    'd': 6,
    'e': 4,
    'f': 11,
    'z': 0
}

def astar(start, goal):

    pq = []
    heapq.heappush(pq, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while pq:

        f, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor, weight in graph[current]:

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]

                heapq.heappush(pq, (priority, neighbor))
                parent[neighbor] = current

    # reconstruct path
    path = []
    node = goal

    while node:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Path:", path)
    print("Cost:", cost[goal])

astar('a', 'z')
