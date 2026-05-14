graph = [

    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 3)
]

def krusk(graph):
    graph.sort(key=lambda x:x[2])

    # print(graph)

    mst = []
    mst_cost = 0
    visited = set()

    for source, destination , cost in graph:

        if  destination not in visited:

            visited.add(source)
            visited.add(destination)

            mst.append((source,destination,cost))

            mst_cost =+ cost

    print("MST : ")

    for s,d,c in mst:
        print(f"{s} -> {d} = {c}")

    print("/nTotal cost of MST : " , mst_cost)
















krusk(graph)