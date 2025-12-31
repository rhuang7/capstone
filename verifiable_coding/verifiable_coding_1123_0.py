import sys
import sys
input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        graph = [set() for _ in range(N)]
        for _ in range(M):
            A = int(data[idx])
            B = int(data[idx+1])
            idx += 2
            graph[A].add(B)
            graph[B].add(A)
        Q = int(data[idx])
        idx += 1
        for _ in range(Q):
            X = int(data[idx])
            Y = int(data[idx+1])
            idx += 2
            visited = set()
            stack = [X]
            visited.add(X)
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            if Y in visited:
                results.append("YO")
            else:
                results.append("NO")
    print('\n'.join(results))
if __name__ == '__main__':
    solve()