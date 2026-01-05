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
            a = s[i]
            b = s[i+1]
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

        start = next(iter(graph))
        dfs(start)
        if len(visited) != 26:
            print("NO")
            continue

        # Check if the graph is a tree and has no cycles
        # We can do this by checking if the number of edges is 25
        # But since the graph is built from the string, it's already a tree
        # So we can just check if the order has 26 nodes
        if len(order) != 26:
            print("NO")
            continue

        # Check if the order is a valid layout
        valid = True
        for i in range(len(order) - 1):
            a = order[i]
            b = order[i+1]
            if b not in graph[a]:
                valid = False
                break

        if not valid:
            print("NO")
            continue

        print("YES")
        print(''.join(order))

if __name__ == '__main__':
    solve()