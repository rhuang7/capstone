import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    words = data[1:N+1]

    from collections import defaultdict

    graph = defaultdict(list)
    word_set = set(words)

    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            w1 = words[i]
            w2 = words[j]
            if can_hop(w1, w2):
                graph[w1].append(w2)

    # Topological sort with longest path
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = []
    for node in word_set:
        if in_degree.get(node, 0) == 0:
            queue.append(node)

    dp = {node: 1 for node in word_set}
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            dp[v] = max(dp[v], dp[u] + 1)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    print(max(dp.values()))

def can_hop(w1, w2):
    if len(w1) == len(w2):
        # Check if w2 is obtained by replacing one letter with a letter to its right that is alphabetically larger
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                # Check if there is a character to the right in w1 that is alphabetically larger than w1[i]
                for j in range(i+1, len(w1)):
                    if w1[j] > w1[i]:
                        return True
                return False
        return False
    elif len(w1) == len(w2) + 1:
        # Check if w2 is obtained by deleting one character from w1
        i = 0
        j = 0
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(w2)
    else:
        return False

if __name__ == '__main__':
    solve()