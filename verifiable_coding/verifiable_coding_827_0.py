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
        
        # Total number of 'a's in the repeated string
        total_a = a_count * K
        
        # Total number of 'b's in the repeated string
        total_b = b_count * K
        
        # Total number of 'ab' subsequences
        # Each 'a' can pair with each 'b' that comes after it
        # So total is (total_a * total_b) - (number of 'a's before 'b's in S * K)
        # But since the string is repeated, we need to calculate how many 'a's are before each 'b' in S
        
        # Precompute for each position in S, the number of 'a's before it
        a_before = [0] * N
        a_count_so_far = 0
        for i in range(N):
            if S[i] == 'a':
                a_count_so_far += 1
            a_before[i] = a_count_so_far
        
        # Precompute for each position in S, the number of 'b's after it
        b_after = [0] * N
        b_count_so_far = 0
        for i in range(N-1, -1, -1):
            if S[i] == 'b':
                b_count_so_far += 1
            b_after[i] = b_count_so_far
        
        # Calculate total 'ab' pairs in one repetition of S
        ab_in_one = 0
        for i in range(N):
            if S[i] == 'b':
                ab_in_one += a_before[i]
        
        # Total 'ab' pairs in K repetitions
        total_ab = ab_in_one * K
        
        # Also, each 'a' in one repetition can pair with each 'b' in other repetitions
        # So add (total_a - a_count) * b_count * K
        total_ab += (total_a - a_count) * b_count * K
        
        results.append(total_ab)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()