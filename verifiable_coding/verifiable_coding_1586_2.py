import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    first_row = list(map(int, data[1:]))
    
    result = []
    
    for shift in range(N):
        current_max = 0
        for i in range(N):
            a = first_row[i]
            b = first_row[(i + shift) % N]
            current_max = max(current_max, a + b)
        result.append(str(current_max))
    
    print(' '.join(result))

if __name__ == '__main__':
    solve()