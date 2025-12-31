import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        from collections import defaultdict
        graph = defaultdict(set)
        for i in range(len(s) - 1):
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
            if char not in visited:
                start = char
                break

        if start is None:
            print("YES")
            print("abcdefghijklmnopqrstuvwxyz")
            continue

        dfs(start)
        order.reverse()

        if len(order) != 26:
            print("NO")
            continue

        valid = True
        for i in range(len(order) - 1):
            a, b = order[i], order[i+1]
            if b not in graph[a] or a not in graph[b]:
                valid = False
                break

        if valid:
            print("YES")
            print("".join(order))
        else:
            print("NO")

if __name__ == '__main__':
    solve()