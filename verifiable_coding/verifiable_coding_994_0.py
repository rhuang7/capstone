import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute prefix sums of A
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        
        # Precompute prefix sums of B (but we don't need to store B)
        # Instead, we use the formula B[i][j] = A[i] + A[j]
        # The sum of a square submatrix from (x1, y1) to (x2, y2) is:
        # sum_{i=x1}^{x2} sum_{j=y1}^{y2} (A[i] + A[j]) 
        # = sum_{i=x1}^{x2} (A[i] * (y2 - y1 + 1) + sum_{j=y1}^{y2} A[j])
        # = (y2 - y1 + 1) * sum_{i=x1}^{x2} A[i] + (x2 - x1 + 1) * sum_{j=y1}^{y2} A[j]
        # = (y2 - y1 + 1) * (prefix[x2] - prefix[x1-1]) + (x2 - x1 + 1) * (prefix[y2] - prefix[y1-1])
        
        # Let k = x2 - x1 = y2 - y1
        # So x2 = x1 + k, y2 = y1 + k
        # The sum becomes:
        # (k + 1) * (prefix[x1 + k] - prefix[x1-1]) + (k + 1) * (prefix[y1 + k] - prefix[y1-1])
        # = (k + 1) * [ (prefix[x1 + k] - prefix[x1-1]) + (prefix[y1 + k] - prefix[y1-1]) ]
        # = (k + 1) * [ (prefix[x1 + k] + prefix[y1 + k]) - (prefix[x1-1] + prefix[y1-1]) ]
        
        # We need this to equal X
        # So for each k from 0 to N-1:
        # We look for pairs (x, y) such that:
        # (k + 1) * [ (prefix[x + k] + prefix[y + k]) - (prefix[x-1] + prefix[y-1]) ] = X
        
        count = 0
        for k in range(N):
            target = X // (k + 1)
            if (k + 1) * target != X:
                continue
            # We need (prefix[x + k] + prefix[y + k]) - (prefix[x-1] + prefix[y-1]) = target
            # Let's compute prefix[x + k] + prefix[y + k] - prefix[x-1] - prefix[y-1]
            # = (prefix[x + k] - prefix[x-1]) + (prefix[y + k] - prefix[y-1])
            # = sum of A from x to x + k and sum of A from y to y + k
            # So for each x in 1..N-k, we compute sumA = prefix[x + k] - prefix[x-1]
            # Then we need sumA + (prefix[y + k] - prefix[y-1]) = target
            # => prefix[y + k] - prefix[y-1] = target - sumA
            # So for each x, we compute sumA and look for how many y's satisfy this
            # We can precompute all possible sumA for x in 1..N-k and store them in a list
            # Then for each sumA, we look for (target - sumA) in the list of sumA's for y
            # But we need to do this efficiently
            # Let's precompute all possible sumA for x in 1..N-k
            sumA_list = []
            for x in range(1, N - k + 1):
                sumA = prefix[x + k] - prefix[x - 1]
                sumA_list.append(sumA)
            # Now for each sumA in sumA_list, we need to find how many times (target - sumA) appears in sumA_list
            # But we need to do this efficiently, so we can use a frequency dictionary
            freq = {}
            for s in sumA_list:
                freq[s] = freq.get(s, 0) + 1
            # Now for each sumA in sumA_list, we check if (target - sumA) is in freq
            # But we need to count the number of pairs (sumA, sumA') such that sumA + sumA' = target
            # So for each sumA, we check if (target - sumA) is in freq, and add the count
            # But we have to avoid double counting (i.e., (sumA, sumA') and (sumA', sumA))
            # So we can use a set to store the pairs
            seen = set()
            for i in range(len(sumA_list)):
                s = sumA_list[i]
                needed = target - s
                if needed in freq:
                    if (s, needed) in seen:
                        continue
                    seen.add((s, needed))
                    count += freq[needed]
            # Also, if s == needed, we need to avoid double counting
            # So we can check if s == needed and add freq[s] choose 2
            # But since we are using a set, we can avoid this by checking if s == needed and adding freq[s] * (freq[s] - 1) // 2
            # But since we are using a set, we can do this separately
            # So we need to check if s == needed and add the combinations
            # But since we are using a set, we can do this after the loop
            # So we can loop through all unique s in sumA_list and check if s == needed
            # But this is not efficient, so we can instead use a frequency dictionary and for each s in freq:
            # if s == needed, then add freq[s] * (freq[s] - 1) // 2
            # But we have to make sure we don't double count
            # So we can do this after the previous loop
            # So we can do this:
            for s in freq:
                needed = target - s
                if s == needed:
                    count += freq[s] * (freq[s] - 1) // 2
            # But we have to make sure we don't double count
            # So we can use a set to track which pairs we've already counted
            # So we can do this:
            # But this is getting complicated, so let's use a different approach
            # We can use a frequency dictionary and for each s in freq:
            # if s <= needed, then add freq[s] * freq[needed]
            # But we have to make sure we don't double count
            # So we can do this:
            # Create a frequency dictionary
            freq = {}
            for s in sumA_list:
                freq[s] = freq.get(s, 0) + 1
            # Now for each s in freq:
            # if s <= needed, then add freq[s] * freq[needed]
            # But we have to make sure we don't double count
            # So we can do this:
            for s in freq:
                needed = target - s
                if needed in freq:
                    if s <= needed:
                        count += freq[s] * freq[needed]
            # But this counts (s, needed) and (needed, s) as separate, which is not correct
            # So we need to make sure that we only count each pair once
            # So we can use a set to track which pairs we've already counted
            seen = set()
            for s in freq:
                needed = target - s
                if needed in freq and (s, needed) not in seen:
                    seen.add((s, needed))
                    seen.add((needed, s))
                    count += freq[s] * freq[needed]
        
        results.append(count)
    
    for res in results:
        print(res)