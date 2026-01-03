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
        # Since it's a circle, we can consider all possible triplets by checking each position
        # and considering the next two positions (wrapping around if needed)
        for i in range(N):
            # Get the current, next, and next-next elements
            j = (i + 1) % N
            k = (i + 2) % N
            current_sum = X[i] + X[j] + X[k]
            if current_sum > max_sum:
                max_sum = current_sum
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()