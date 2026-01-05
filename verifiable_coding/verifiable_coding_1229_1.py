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
        
        # Calculate initial scores
        motu_score = 0
        tomu_score = 0
        for i in range(N):
            if i % 2 == 0:
                motu_score += A[i]
            else:
                tomu_score += A[i]
        
        # If Tomu already wins, output YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # We need to perform swaps to make Tomu's score greater
        # We can only swap elements at even indices (Motu's turn) with elements at odd indices (Tomu's turn)
        # Because swapping an even index with an odd index will change the scores of both players
        
        # Create a list of pairs (value, index) for even indices and odd indices
        even = []
        odd = []
        for i in range(N):
            if i % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        
        # Sort even in ascending order and odd in descending order
        even.sort()
        odd.sort(reverse=True)
        
        # Try to swap the best possible elements
        # For each swap, we take the smallest even and largest odd
        # and swap them
        # We can do this up to K times
        for i in range(min(K, len(even), len(odd))):
            # Swap even[i] (smallest even) with odd[i] (largest odd)
            # This will increase Tomu's score and decrease Motu's score
            motu_score -= even[i]
            tomu_score += even[i]
            motu_score += odd[i]
            tomu_score -= odd[i]
        
        if tomu_score > motu_score:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()