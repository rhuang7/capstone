import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    words = data[1:N+1]

    from collections import defaultdict

    # Preprocess words
    word_set = set(words)
    word_list = list(word_set)

    # Build graph
    graph = defaultdict(list)

    for i in range(len(word_list)):
        word = word_list[i]
        for j in range(len(word_list)):
            if i == j:
                continue
            other_word = word_list[j]
            if can_hop(word, other_word):
                graph[word].append(other_word)

    # Topological sort using Kahn's algorithm
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = []
    for word in word_set:
        if in_degree.get(word, 0) == 0:
            queue.append(word)

    max_length = 0
    while queue:
        current = queue.pop(0)
        max_length += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    print(max_length)

def can_hop(w1, w2):
    # Check if w2 can be obtained from w1 by deleting one letter
    if len(w2) == len(w1) - 1:
        i = 0
        j = 0
        while i < len(w1) and j < len(w2):
            if w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(w2)

    # Check if w2 can be obtained from w1 by replacing one letter
    if len(w1) != len(w2):
        return False
    diff = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diff += 1
            if diff > 1:
                return False
    if diff == 1:
        # Check if the replacement is valid
        i = w1.index(w2[0])
        for j in range(i + 1, len(w1)):
            if w1[j] == w2[i]:
                return True
    return False