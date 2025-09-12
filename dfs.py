#depth first search

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[],
    'G':[],
}
visited=set()

def dfs(visited,graph,node):
    
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited,graph,node)
