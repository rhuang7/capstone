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
        
        # Check all possible triplets of friends
        for i in range(N):
            # Check triplet (i, i+1, i+2)
            sum1 = X[i] + X[(i+1)%N] + X[(i+2)%N]
            if sum1 > max_sum:
                max_sum = sum1
            # Check triplet (i, i-1, i-2)
            sum2 = X[i] + X[(i-1)%N] + X[(i-2)%N]
            if sum2 > max_sum:
                max_sum = sum2
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()