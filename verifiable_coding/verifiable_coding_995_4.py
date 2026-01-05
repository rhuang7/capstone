import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    A = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    
    left = [0] * n
    right = [0] * n
    
    left[0] = A[0]
    for i in range(1, n):
        left[i] = left[i-1] + A[i]
    
    right[-1] = A[-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] + A[i]
    
    max_money = 0
    for i in range(k+1):
        if i <= n and (n - i) >= k - i:
            total = left[i] + right[n - k + i]
            if total > max_money:
                max_money = total
    
    print(max_money)

if __name__ == '__main__':
    solve()