import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    words = data[1:N+1]

    word_set = set(words)
    word_list = list(word_set)

    # Preprocess: create a dictionary mapping each word to its index
    word_to_idx = {word: i for i, word in enumerate(word_list)}

    # Precompute all possible hops for each word
    graph = defaultdict(list)

    for i, word in enumerate(word_list):
        # Hop by deleting one letter
        for j in range(len(word)):
            new_word = word[:j] + word[j+1:]
            if new_word in word_set:
                graph[i].append(word_to_idx[new_word])

        # Hop by replacing one letter with a letter to its right that is alphabetically larger
        for j in range(len(word)):
            for k in range(j+1, len(word)):
                if word[k] > word[j]:
                    new_word = word[:j] + word[k] + word[j+1:k] + word[k+1:]
                    if new_word in word_set:
                        graph[i].append(word_to_idx[new_word])

    # Longest path in a DAG (using topological sort)
    # Since the graph is directed acyclic (no cycles possible due to hop rules), we can use topological sort
    # However, for small N (<= 100), we can use DFS-based approach for longest path

    # Use memoization for DFS
    memo = [-1] * len(word_list)

    def dfs(u):
        if memo[u] != -1:
            return memo[u]
        max_len = 1
        for v in graph[u]:
            if v != u:
                current_len = 1 + dfs(v)
                if current_len > max_len:
                    max_len = current_len
        memo[u] = max_len
        return max_len

    max_hopping_number = 0
    for i in range(len(word_list)):
        max_hopping_number = max(max_hopping_number, dfs(i))

    print(max_hopping_number)