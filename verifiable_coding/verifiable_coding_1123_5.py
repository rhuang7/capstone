import sys
import sys
input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        graph = [set() for _ in range(N)]
        for _ in range(M):
            a = int(data[idx])
            b = int(data[idx+1])
            graph[a].add(b)
            graph[b].add(a)
            idx += 2
        Q = int(data[idx])
        idx += 1
        results = []
        for _ in range(Q):
            x = int(data[idx])
            y = int(data[idx+1])
            idx += 2
            visited = set()
            stack = [x]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            if y in visited:
                results.append("YO")
            else:
                results.append("NO")
        print('\n'.join(results))
if __name__ == '__main__':
    solve()