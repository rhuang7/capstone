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
        total = 0
        
        for c in S:
            if c == 'a':
                count_a += 1
            elif c == 'b':
                total += count_a
        
        # Now calculate the contribution from the repeated string
        # For each 'a' in the original string, it contributes count_b * K
        # For each 'b' in the original string, it contributes count_a * K
        # But we need to account for the fact that each 'a' in the original string appears K times
        # and each 'b' in the original string appears K times
        
        # Total number of 'a's in the new string is count_a * K
        # Total number of 'b's in the new string is count_b * K
        
        # The number of 'ab' pairs is (count_a * K) * (count_b * K)
        # But we also need to account for the pairs between the original string and the repeated copies
        
        # The initial total is the number of 'ab' pairs in the original string
        # Then, for each additional copy, we add (count_a * count_b) * K
        # Because each 'a' in the original string contributes count_b * K
        # and each 'b' in the original string contributes count_a * K
        
        # So the total is:
        # initial_total + (count_a * count_b) * (K - 1) * K
        
        # But wait, the initial total is the number of 'ab' pairs in the original string
        # which is already calculated as 'total'
        # Then, for each of the K-1 additional copies, we add (count_a * count_b) * K
        # Because each 'a' in the original string contributes count_b * K
        # and each 'b' in the original string contributes count_a * K
        
        # So the total is:
        # total + (count_a * count_b) * K * (K - 1)
        
        # But wait, the original string has count_a 'a's and count_b 'b's
        # So the number of 'ab' pairs between the original string and each copy is count_a * count_b
        # And there are K copies, so the total is count_a * count_b * K
        # But we already counted the pairs within the original string, so we need to multiply by (K-1)
        
        # So the correct formula is:
        # total + count_a * count_b * K * (K - 1)
        
        # But wait, the initial total is already the number of 'ab' pairs in the original string
        # So the total is:
        # total + count_a * count_b * K * (K - 1)
        
        # So the final answer is:
        # total + count_a * count_b * K * (K - 1)
        
        # However, this is incorrect because the original string's 'a's and 'b's are repeated K times
        # So the total number of 'a's is count_a * K and the total number of 'b's is count_b * K
        # The total number of 'ab' pairs is (count_a * K) * (count_b * K)
        # But this counts all pairs, including those within the original string
        # So the correct formula is:
        # (count_a * K) * (count_b * K) - total
        
        # Because total is the number of 'ab' pairs in the original string
        # So the total number of 'ab' pairs in the new string is:
        # (count_a * K) * (count_b * K) - total
        
        # So the final answer is:
        # (count_a * K) * (count_b * K) - total
        
        # So we calculate this and add it to the results
        
        total_ab = (count_a * K) * (count_b * K) - total
        results.append(str(total_ab))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()