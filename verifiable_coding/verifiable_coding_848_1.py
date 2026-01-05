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
        X = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_sum = 0
        
        # Check all possible triplets of 3 consecutive students
        for i in range(N):
            # Consider i, i+1, i+2 (mod N)
            sum_ = X[i] + X[(i+1) % N] + X[(i+2) % N]
            if sum_ > max_sum:
                max_sum = sum_
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()