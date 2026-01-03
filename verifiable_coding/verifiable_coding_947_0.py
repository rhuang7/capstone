import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    words = data[1:N+1]

    # Preprocess words
    word_set = set(words)
    word_list = list(word_set)

    # Create a graph where each node is a word and edges represent a hop
    graph = defaultdict(list)

    def can_hop(w1, w2):
        # Case 1: w2 is obtained by deleting one letter from w1
        if len(w2) == len(w1) - 1:
            return w2 in [w1[:i] + w1[i+1:] for i in range(len(w1))]
        # Case 2: w2 is obtained by replacing one letter in w1 with a letter to its right that is alphabetically larger
        if len(w1) == len(w2):
            for i in range(len(w1)):
                for j in range(i+1, len(w1)):
                    if w1[j] > w1[i]:
                        if w2 == w1[:i] + w1[j] + w1[i+1:j] + w1[j+1:]:
                            return True
            return False
        return False

    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if i != j and can_hop(word_list[i], word_list[j]):
                graph[word_list[i]].append(word_list[j])

    # Longest path in a DAG (topological sort + DP)
    # Since words can have same length, we need to process them in order of increasing length
    # Sort words by length
    sorted_words = sorted(word_list, key=lambda x: len(x))

    # Topological sort
    in_degree = {word: 0 for word in sorted_words}
    for u in graph:
        for v in graph[u]:
            if v in in_degree:
                in_degree[v] += 1

    queue = deque([word for word in sorted_words if in_degree[word] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # DP to find longest path
    dp = {word: 1 for word in sorted_words}
    for u in topo_order:
        for v in graph[u]:
            if dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1

    print(max(dp.values()))

if __name__ == '__main__':
    solve()