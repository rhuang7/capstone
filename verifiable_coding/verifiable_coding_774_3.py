import sys

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
    
    def can_send(a, b):
        if a == b:
            return True
        left = a
        right = b
        while left < right:
            mid = (left + right) // 2
            if A[mid] - A[a] <= K:
                left = mid + 1
            else:
                right = mid
        return A[right] - A[a] <= K
    
    for a, b in queries:
        if can_send(a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()