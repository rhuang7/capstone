import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        from collections import defaultdict
        graph = defaultdict(set)
        for i in range(len(s)-1):
            a, b = s[i], s[i+1]
            graph[a].add(b)
            graph[b].add(a)

        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            order.append(node)

        start = None
        for char in graph:
            if len(graph[char]) == 0:
                start = char
                break
        if start is None:
            start = next(iter(graph))

        dfs(start)
        order.reverse()

        if len(order) != 26:
            print("NO")
            continue

        result = ''.join(order)
        print("YES")
        print(result)

if __name__ == '__main__':
    solve()