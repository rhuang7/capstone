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
        K = int(data[idx+1])
        idx += 2
        S = data[idx]
        idx += 1
        
        # Precompute counts of 'a' and 'b' in S
        a_count = S.count('a')
        b_count = S.count('b')
        
        # Total number of 'a's in K repetitions
        total_a = a_count * K
        
        # Total number of 'b's in K repetitions
        total_b = b_count * K
        
        # Number of 'ab' subsequences in one repetition of S
        ab_in_one = 0
        a_in_run = 0
        for c in S:
            if c == 'a':
                a_in_run += 1
            elif c == 'b':
                ab_in_one += a_in_run
        
        # Total number of 'ab' subsequences in K repetitions
        total_ab = ab_in_one * K
        
        # Add cross terms between different repetitions
        # For each 'a' in one repetition and 'b' in another
        cross_ab = a_count * b_count * (K * (K - 1)) // 2
        
        total_ab += cross_ab
        
        results.append(total_ab)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()