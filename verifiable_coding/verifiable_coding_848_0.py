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
            if i + 2 < N:
                current_sum = X[i] + X[i+1] + X[i+2]
                if current_sum > max_sum:
                    max_sum = current_sum
            # Check triplet (i, i-1, i-2)
            if i - 2 >= 0:
                current_sum = X[i] + X[i-1] + X[i-2]
                if current_sum > max_sum:
                    max_sum = current_sum
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()