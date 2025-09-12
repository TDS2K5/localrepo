graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[],
}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m)

        for neigbour in graph[m]:
            if neigbour not in visited:
                visited.append(neigbour)
                queue.append(neigbour)

for k,v in graph.items():
    print(k,v)
bfs(visited,graph,'A')