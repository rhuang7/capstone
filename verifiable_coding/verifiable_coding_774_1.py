import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    P = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    
    queries = []
    for _ in range(P):
        a = int(data[idx]) - 1
        idx += 1
        b = int(data[idx]) - 1
        idx += 1
        queries.append((a, b))
    
    A.sort()
    
    for a, b in queries:
        if a == b:
            print("Yes")
            continue
        if abs(A[a] - A[b]) <= K:
            print("Yes")
        else:
            print("No")
            
if __name__ == '__main__':
    solve()