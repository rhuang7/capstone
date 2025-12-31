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
        
        # Check all possible triplets in the circle
        for i in range(N):
            # Consider the current element and the next two elements
            # Since it's a circle, wrap around
            j = (i + 1) % N
            k = (i + 2) % N
            current_sum = X[i] + X[j] + X[k]
            if current_sum > max_sum:
                max_sum = current_sum
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()