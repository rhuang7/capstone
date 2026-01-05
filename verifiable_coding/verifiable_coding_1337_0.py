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
        P = list(map(int, data[idx:idx+N]))
        idx += N
        R = int(data[idx])
        idx += 1
        
        min_p = min(P)
        if R >= min_p:
            results.append(-1)
            continue
        
        # The minimum number of candies is R + (min_p) * 1
        # Because each person must get at least 1 candy, and there must be R left
        # So the minimum is R + min_p
        results.append(R + min_p)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()