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
        
        # If Tomu already wins, answer is YES
        if tomu_score > motu_score:
            results.append("YES")
            continue
        
        # If Tomu cannot win even with K swaps, answer is NO
        if K == 0:
            results.append("NO")
            continue
        
        # Prepare list of elements and their positions
        elements = [(A[i], i) for i in range(N)]
        
        # Sort elements by value in descending order
        elements.sort(reverse=True)
        
        # Try to swap elements to maximize Tomu's score and minimize Motu's score
        # We can only swap elements at odd positions (Tomu's turns) with elements at even positions (Motu's turns)
        # Because Tomu can only perform up to K swaps
        # We will try to find the best K swaps to maximize the difference (Tomu - Motu)
        
        # Calculate the initial difference
        diff = tomu_score - motu_score
        
        # We will try to maximize the difference by swapping elements
        # For each possible swap, we can calculate the gain in difference
        # We will use a greedy approach to select the best swaps
        
        # Create a list of possible swaps
        swaps = []
        for i in range(N):
            if i % 2 == 0:  # Motu's turn
                for j in range(i + 1, N):
                    if j % 2 == 1:  # Tomu's turn
                        # Calculate the gain if we swap A[i] and A[j]
                        gain = (A[j] - A[i]) - (A[i] - A[j])  # (Tomu gains A[j] - A[i], Motu loses A[i] - A[j])
                        swaps.append((gain, i, j))
        
        # Sort swaps by gain in descending order
        swaps.sort(reverse=True)
        
        # Apply up to K best swaps
        for gain, i, j in swaps:
            if K <= 0:
                break
            # Swap A[i] and A[j]
            A[i], A[j] = A[j], A[i]
            # Recalculate scores
            motu_score = 0
            tomu_score = 0
            for idx in range(N):
                if idx % 2 == 0:
                    motu_score += A[idx]
                else:
                    tomu_score += A[idx]
            diff = tomu_score - motu_score
            K -= 1
        
        if diff > 0:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)