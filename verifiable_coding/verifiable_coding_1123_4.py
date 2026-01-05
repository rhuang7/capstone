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
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            if Y in visited:
                print("YO")
            else:
                print("NO")
if __name__ == '__main__':
    solve()