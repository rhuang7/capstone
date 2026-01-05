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
        N, M, S = map(int, data[idx:idx+3])
        idx += 3
        H = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the hours in ascending order to try to fit as many topics as possible
        H.sort()
        
        count = 0
        for h in H:
            if h > S:
                continue
            count += 1
            if count > M:
                break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()