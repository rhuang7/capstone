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

    def can_hop(w1, w2):
        if len(w2) == len(w1) - 1:
            return w2 in w1
        if len(w2) == len(w1):
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    for j in range(i+1, len(w1)):
                        if w1[j] > w1[i] and w2[i] == w1[j]:
                            return True
                    return False
            return False
        return False

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and can_hop(words[i], words[j]):
                graph[words[i]].append(words[j])

    from collections import deque
    max_len = 0
    visited = set()

    for word in words:
        if word not in visited:
            queue = deque()
            queue.append((word, 1))
            visited.add(word)
            while queue:
                current, length = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                max_len = max(max_len, length)

    print(max_len)

if __name__ == '__main__':
    solve()