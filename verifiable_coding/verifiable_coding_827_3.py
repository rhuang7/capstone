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
        
        # Total number of 'ab' pairs is total_a * total_b
        # But we need to consider the order in the original string
        # So we need to count the number of 'a's before each 'b' in the original string
        # and multiply by K (since the string is repeated K times)
        
        # Count the number of 'a's before each 'b' in the original string
        a_before_b = 0
        a_count_in_s = 0
        for c in S:
            if c == 'a':
                a_count_in_s += 1
            elif c == 'b':
                a_before_b += a_count_in_s
        
        # Total number of 'ab' pairs in K repetitions
        total_ab = a_before_b * K * K
        
        results.append(total_ab)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()