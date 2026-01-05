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
        
        A.sort()
        min_sum = 0
        prev = 0
        for num in A:
            if num > prev:
                min_sum += prev
                prev = num
            else:
                prev = num
        results.append(str(min_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()