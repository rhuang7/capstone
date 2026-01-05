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
    # Use memoization for longest path
    memo = {}

    def longest_path(node):
        if node in memo:
            return memo[node]
        max_len = 1
        for neighbor in graph[node]:
            if neighbor not in memo:
                temp = 1 + longest_path(neighbor)
            else:
                temp = 1 + memo[neighbor]
            if temp > max_len:
                max_len = temp
        memo[node] = max_len
        return max_len

    # Find the maximum value in memo
    max_hopping = 0
    for word in word_set:
        if word in memo:
            if memo[word] > max_hopping:
                max_hopping = memo[word]

    print(max_hopping)

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
    if len(w1) == len(w2):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                # Check if w2[i] appears to the right of w1[i] in w1 and is alphabetically after w1[i]
                for j in range(i+1, len(w1)):
                    if w1[j] == w2[i] and w2[i] > w1[i]:
                        return True
                return False
        return True
    return False