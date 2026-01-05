import sys
import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        graph = [[] for _ in range(N)]
        for _ in range(M):
            a = int(data[idx])
            b = int(data[idx+1])
            graph[a].append(b)
            graph[b].append(a)
            idx += 2
        visited = [False] * N
        count = 0
        for i in range(N):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()