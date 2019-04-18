from collections import defaultdict

def dfs(graph, N, key, footprint):
    print(footprint)
    if len(footprint) == N + 1:
        return footprint
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)
        tmp = footprint[:]
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)
        # 원상복구
        graph[key].insert(idx, country) # insert : idx위치에 country 삽입!
        if ret:
            return ret

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(tickets)

    for t in tickets:
        graph[t[0]].append(t[1])
        graph[t[0]].sort()
    print(graph)
    answer = dfs(graph, N, 'ICN', ['ICN'])
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))