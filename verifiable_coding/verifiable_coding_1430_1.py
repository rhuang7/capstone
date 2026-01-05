import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 0:
            results.append(N)
            continue
        
        # The minimum configuration is to have each kid get 1 candy, and then increase every other kid by 1
        # to ensure a difference of at least K between adjacent kids
        # This is a pattern that repeats every 2 kids
        # So the total is N + (N // 2) * K
        # But since it's a circle, we need to ensure the first and last kid also have a difference of at least K
        # So we need to add an extra K if N is even
        if N % 2 == 0:
            total = N + (N // 2) * K + K
        else:
            total = N + (N // 2) * K
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()