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
        result = []

        def dfs(node, parent):
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor != parent and neighbor not in visited:
                    dfs(neighbor, node)

        start = next(iter(graph))
        dfs(start, -1)

        if len(visited) != 26:
            print("NO")
        else:
            print("YES")
            print(''.join(result))

if __name__ == '__main__':
    solve()