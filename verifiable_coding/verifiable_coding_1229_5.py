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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute initial scores
        motu_score = 0
        tomu_score = 0
        for i in range(0, N, 2):
            motu_score += A[i]
        for i in range(1, N, 2):
            tomu_score += A[i]
        
        # If Tomu already wins, answer is YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # If Tomu cannot win even with K swaps, answer is NO
        if K == 0:
            results.append("NO")
            continue
        
        # We can perform swaps to increase Tomu's score and decrease Motu's score
        # We need to find the best K swaps to maximize (Tomu's score - Motu's score)
        # We can do this by comparing the elements at even and odd positions
        # For each even position (Motu's turn), if we can swap it with an odd position (Tomu's turn) with a smaller value, it helps Tomu
        # For each odd position (Tomu's turn), if we can swap it with an even position (Motu's turn) with a larger value, it helps Tomu
        
        # Create a list of pairs (even index, value), (odd index, value)
        even = []
        odd = []
        for i in range(N):
            if i % 2 == 0:
                even.append((i, A[i]))
            else:
                odd.append((i, A[i]))
        
        # Sort even indices by value (ascending), odd indices by value (descending)
        even.sort(key=lambda x: x[1])
        odd.sort(key=lambda x: -x[1])
        
        # Try to perform swaps
        i = 0
        j = 0
        swaps = 0
        while i < len(even) and j < len(odd) and swaps < K:
            # Compare even[i] and odd[j]
            even_val = even[i][1]
            odd_val = odd[j][1]
            if even_val > odd_val:
                # Swap them to increase Tomu's score and decrease Motu's score
                # This is beneficial
                swaps += 1
                i += 1
                j += 1
            else:
                # No benefit, break
                break
        
        # After performing swaps, check if Tomu's score is greater than Motu's
        # Recompute scores with the swaps
        # We need to simulate the swaps
        # Create a copy of A
        A_copy = A[:]
        # Perform the swaps
        i = 0
        j = 0
        swaps = 0
        while i < len(even) and j < len(odd) and swaps < K:
            even_val = even[i][1]
            odd_val = odd[j][1]
            if even_val > odd_val:
                # Swap the values
                A_copy[even[i][0]] = odd_val
                A_copy[odd[j][0]] = even_val
                swaps += 1
                i += 1
                j += 1
            else:
                # No benefit, break
                break
        
        # Recompute scores
        motu_score = 0
        tomu_score = 0
        for i in range(0, N, 2):
            motu_score += A_copy[i]
        for i in range(1, N, 2):
            tomu_score += A_copy[i]
        
        if tomu_score > motu_score:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)