import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    max_val = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                current = A[i] % A[j]
                if current > max_val:
                    max_val = current
    print(max_val)

if __name__ == '__main__':
    solve()