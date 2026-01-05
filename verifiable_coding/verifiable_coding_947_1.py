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

    # Topological sort with longest path
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Initialize queue with nodes of in_degree 0
    queue = []
    for word in word_set:
        if in_degree.get(word, 0) == 0:
            queue.append(word)

    # Longest path using priority queue (Dijkstra's algorithm)
    # Since we want the longest path, we use a max-heap
    # We'll use a max-heap by storing negative values
    max_heap = []
    for word in queue:
        heapq.heappush(max_heap, (-1, word))

    # Dictionary to store the longest path length for each node
    longest_path = {word: 1 for word in word_set}

    while max_heap:
        neg_len, word = heapq.heappop(max_heap)
        current_len = -neg_len

        for neighbor in graph[word]:
            if longest_path[neighbor] < current_len + 1:
                longest_path[neighbor] = current_len + 1
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    heapq.heappush(max_heap, (-(current_len + 1), neighbor))

    print(max(longest_path.values()))

def can_hop(w1, w2):
    # Check if w2 can be obtained from w1 by deleting one letter
    if len(w2) == len(w1) - 1:
        return w2 in w1
    # Check if w2 can be obtained from w1 by replacing one letter
    if len(w2) == len(w1):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                # Check if the replacement is valid
                for j in range(i+1, len(w1)):
                    if w1[j] > w1[i] and w2[i] == w1[j]:
                        return True
                return False
    return False