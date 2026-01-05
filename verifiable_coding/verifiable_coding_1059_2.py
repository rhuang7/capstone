import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    
    max_val = 0
    min_val = float('inf')
    
    for num in A:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    if min_val == max_val:
        print(0)
        return
    
    for num in A:
        if num != min_val:
            max_val = max(max_val, num % min_val)
    
    print(max_val)

if __name__ == '__main__':
    solve()