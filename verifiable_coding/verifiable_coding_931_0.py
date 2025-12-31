import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        values = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = 0
        for num in values:
            if num & 1 == 0:
                total += num
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()