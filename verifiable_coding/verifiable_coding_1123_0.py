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
        for _ in range(Q):
            x = int(data[idx])
            y = int(data[idx+1])
            idx += 2
            visited = [False]*N
            stack = [x]
            visited[x] = True
            while stack:
                current = stack.pop()
                if current == y:
                    print("YO")
                    break
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            else:
                print("NO")
if __name__ == '__main__':
    solve()