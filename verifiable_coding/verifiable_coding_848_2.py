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
        
        # Check all possible triplets in the circular array
        # Since each element has 4 friends, we need to check all possible combinations
        # of 3 elements that are at most 4 positions apart in either direction
        
        for i in range(N):
            # Check all possible triplets starting at i
            for j in range(i+1, min(i+5, N)):
                for k in range(j+1, min(j+5, N)):
                    # Ensure the triplet is valid (not overlapping more than 4 positions)
                    if k - i > 4:
                        continue
                    current_sum = X[i] + X[j] + X[k]
                    if current_sum > max_sum:
                        max_sum = current_sum
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()