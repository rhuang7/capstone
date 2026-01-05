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
        
        count = 0
        
        for i in range(N):
            # Consider the previous 5 days, but not less than 0
            start = max(0, i - 5)
            # Check if current price is strictly smaller than all previous 5 days
            is_good = True
            for j in range(start, i):
                if P[i] >= P[j]:
                    is_good = False
                    break
            if is_good:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()