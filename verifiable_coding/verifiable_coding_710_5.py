import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    max_score = -float('inf')
    
    for i in range(2, N):
        for j in range(i-1, 0, -1):
            for k in range(j-1, -1, -1):
                current = A[k] - A[j] + A[i] - A[k]
                if current > max_score:
                    max_score = current
    
    print(max_score)

if __name__ == '__main__':
    solve()