# Adjacency list
# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# 넓이 우선 탐색
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

# 두 노드간 가능한 모든 경로
def bfs_paths(graph, start, goal):
    result = []
    queue = [(start,[start])]
    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result

# 깊이 우선 탐색
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []
    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))
    return result


# test
print(bfs_paths(graph, 'A', 'F'))
print(bfs_paths(graph, 'D', 'F'))

print(dfs_paths(graph, 'A', 'F'))
print(dfs_paths(graph, 'D', 'F'))