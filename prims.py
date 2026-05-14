import heapq

graph = {

    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',2), ('D',5)],
    'C': [('A',4), ('B',2), ('D',3)],
    'D': [('B',5), ('C',3)]
}

def prims(graph , root):

    q = []
    heapq.heappush(q,(0,root,root))

    visited = set()

    mst = []

    total_cost = 0

    while q:

        cost , source , destination = heapq.heappop(q)

        if destination not in visited :

            visited.add(destination)
            mst.append((source,destination,cost))

            total_cost += cost

            for neighbour , weight in graph[destination]:

                heapq.heappush(q,(weight,source,neighbour))

    print("MST : ")

    for s,d,c in mst:
        print(f"{s}-->{d} ={c}")

    print("\nTotal cost = ",total_cost)

            
            
            










prims(graph,'A')