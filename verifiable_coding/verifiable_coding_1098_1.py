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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        A.sort(reverse=True)
        total = 0
        turn = 0
        for stones in A:
            if turn % 2 == 0:
                total += stones
            turn += 1
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()