import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    max_val = 0
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] > max_val:
                max_val = a[i] % a[j]
    print(max_val)

if __name__ == '__main__':
    solve()