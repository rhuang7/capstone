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
        
        # Initial scores
        motu_score = 0
        tomu_score = 0
        
        # Calculate initial scores
        for i in range(N):
            if i % 2 == 0:
                motu_score += A[i]
            else:
                tomu_score += A[i]
        
        # If Tomu already wins, output YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # We need to perform swaps to make Tomu's score > Motu's
        # We will try to find the best swaps to maximize Tomu's score and minimize Motu's
        
        # Create a list of pairs (index, value)
        elements = [(i, A[i]) for i in range(N)]
        
        # Sort elements by value (descending) for Tomu's benefit
        elements.sort(key=lambda x: (-x[1], x[0]))
        
        # We will try to swap elements in positions where Motu takes them
        # So we look for elements at even indices (Motu's turn) that can be swapped with elements at odd indices (Tomu's turn)
        # We will try to find the best swaps to maximize the difference (Tomu - Motu)
        
        # We will try to perform up to K swaps
        # We will track the current difference (Tomu - Motu)
        diff = tomu_score - motu_score
        
        # We will iterate through the elements and try to find the best swaps
        # We will use a priority queue to find the best swaps
        # We will use a max heap to find the best swaps
        
        # We will create a list of possible swaps
        swaps = []
        for i in range(N):
            if i % 2 == 0:
                # Motu's turn, we can swap this element with an element at odd index
                for j in range(i+1, N):
                    if j % 2 == 1:
                        # Swap elements at i and j
                        # The difference would be: (A[j] - A[i]) * 2
                        swaps.append((-(A[j] - A[i]), i, j))
        
        # Sort the swaps by the potential gain (descending)
        swaps.sort()
        
        # Try to perform up to K swaps
        for i in range(min(K, len(swaps))):
            gain, a, b = swaps[i]
            # Swap elements at a and b
            # The gain is (A[b] - A[a]) * 2
            # Because Motu loses A[a] and gains A[b], Tomu loses A[b] and gains A[a]
            # So the difference (Tomu - Motu) changes by (A[b] - A[a]) * 2
            diff += (A[b] - A[a]) * 2
            if diff > 0:
                results.append("YES")
                break
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()