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

        # Try starting with each character
        found = False
        for start in graph:
            if start not in visited:
                dfs(start)
                if len(order) == 26:
                    found = True
                    break
                visited = set()
        if not found:
            print("NO")
            continue

        # Check if the order is valid
        valid = True
        for i in range(len(order)-1):
            a, b = order[i], order[i+1]
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