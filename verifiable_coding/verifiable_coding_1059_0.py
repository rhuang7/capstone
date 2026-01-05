import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    max_val = 0
    
    # Sort the array
    A.sort()
    
    # For each element, try to find the best divisor
    for i in range(N):
        # Try to find the best divisor for A[i]
        for j in range(N):
            if A[i] % A[j] > max_val:
                max_val = A[i] % A[j]
    
    print(max_val)

if __name__ == '__main__':
    solve()