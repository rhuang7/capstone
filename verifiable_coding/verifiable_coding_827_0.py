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
        
        count_a = 0
        count_b = 0
        total_ab = 0
        
        for c in S:
            if c == 'a':
                count_a += 1
            elif c == 'b':
                total_ab += count_a
        
        # Now calculate the contribution from each repetition
        # For each 'a' in the original string, it contributes to all 'b's in the next K-1 repetitions
        # And also to all 'b's in the same repetition (but already counted in total_ab)
        # So total_ab is the contribution from the same repetition
        # The rest is from the other repetitions
        
        # Total number of 'a's in the new string is count_a * K
        # Total number of 'b's in the new string is count_b * K
        # But we need to calculate how many 'a's are before each 'b' in the new string
        
        # The number of 'a's before each 'b' in the original string is count_a
        # But in the new string, each 'b' is repeated K times, and each 'a' is repeated K times
        # So the total number of 'ab' pairs is:
        # (number of 'a's in original string) * (number of 'b's in original string) * K * (K - 1) / 2
        # But this is not correct, because the 'a's and 'b's are not necessarily in order
        
        # The correct way is to calculate the number of 'a's before each 'b' in the original string
        # and multiply by K (for the number of repetitions)
        # Also, each 'a' in the original string contributes to all 'b's in the next K-1 repetitions
        
        # So the total is:
        # total_ab * K + count_a * count_b * (K - 1)
        
        # Because:
        # - total_ab is the number of 'ab' pairs in the original string
        # - each 'a' in the original string contributes to all 'b's in the next K-1 repetitions
        #   which is count_a * count_b * (K - 1)
        
        total = total_ab * K + count_a * count_b * (K - 1)
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()