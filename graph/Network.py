def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


def solution(n, computers):
    answer = 0
    graph = {}
    remain = []
    for i in range(len(computers)):
        computers[i] = set([(j + 1) for j in list(range(n)) if computers[i][j] != 0])
        computers[i].discard(i + 1)
        graph[i + 1] = computers[i]
        remain.append(i + 1)

    while remain:
        visit = bfs(graph, remain[0])
        answer += 1
        for v in visit:
            if v in remain:
                remain.remove(v)
    return answer