def check_word(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    if count == len(word1) - 1:
        return True
    else:
        return False

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


def solution(begin, target, words):
    answer = 0
    graph = {}
    tmp = []
    for i in range(len(words)):
        if check_word(begin, words[i]):
            tmp.append(words[i])
    graph[begin] = set(tmp)
    for i in range(len(words)):
        tmp = []
        for j in range(len(words)):
            if i == j:
                continue
            if check_word(words[i], words[j]):
                tmp.append(words[j])
        graph[words[i]] = set(tmp)
    paths = dfs_paths(graph, begin, target)
    if len(paths) == 0:
        return 0
    else:
        result = [len(p) for p in paths]
        return min(result) - 1
    # return min(length)