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
        a_count = 0
        b_count = 0
        for c in S:
            if c == 'a':
                a_count += 1
            elif c == 'b':
                b_count += 1
        
        # Total 'a's in the repeated string
        total_a = a_count * K
        # Total 'b's in the repeated string
        total_b = b_count * K
        
        # Total number of 'ab' subsequences
        # Each 'a' can pair with each 'b' that comes after it
        # So total is (total_a * total_b) - (number of 'a's before 'b's in S * K)
        # But we need to calculate the number of 'a's before each 'b' in S
        
        # Count for each position in S: number of 'a's before it
        a_before = 0
        b_after = 0
        for c in S:
            if c == 'a':
                a_before += 1
            elif c == 'b':
                b_after += a_before
        
        # Total 'ab' pairs in one repetition of S
        ab_in_S = b_after
        
        # Total 'ab' pairs in K repetitions
        total_ab = ab_in_S * K + (total_a * total_b - ab_in_S * K)
        
        results.append(str(total_ab))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()