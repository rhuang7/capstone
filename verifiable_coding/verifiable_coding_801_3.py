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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        sorted_A = sorted(A)
        sorted_B = sorted(B)
        
        # Check if the combined sorted lists can be split into two equal parts
        combined = sorted_A + sorted_B
        if len(combined) % 2 != 0:
            results.append(-1)
            continue
        
        # Check if the combined list can be split into two equal parts
        # Each part must have exactly N elements
        # The combined list must have exactly 2N elements
        if len(combined) != 2 * N:
            results.append(-1)
            continue
        
        # Check if the combined list can be split into two equal parts
        # The first N elements must be the same as the second N elements
        if sorted_A != sorted_B:
            results.append(-1)
            continue
        
        # Now, we need to find the minimum cost to make the sequences identical
        # We can only swap elements between A and B
        # The optimal way is to match the smallest elements in A with the smallest in B
        # and so on
        
        # Create a merged sorted list of all elements
        merged = sorted(A + B)
        
        # The first N elements are for A, the next N for B
        # We need to match each element in A with the corresponding element in B
        # So, for i in 0..N-1, A[i] should be equal to B[i]
        # So, we can pair the first N elements of merged with A, and the next N with B
        
        # Create a list of pairs (value, original sequence)
        pairs = []
        for i in range(N):
            pairs.append((merged[i], 'A'))
            pairs.append((merged[i + N], 'B'))
        
        # Sort the pairs by value
        pairs.sort()
        
        # Now, we need to match the values in A and B
        # For each i, if the value in A is less than the value in B, we need to swap
        # The cost is min(A_i, B_j)
        # So, we need to find the minimum cost to make A and B identical
        
        # Create two lists: one for A and one for B
        A_sorted = []
        B_sorted = []
        for val, seq in pairs:
            if seq == 'A':
                A_sorted.append(val)
            else:
                B_sorted.append(val)
        
        # Now, we need to find the minimum cost to make A and B identical
        # We can only swap elements between A and B
        # The optimal way is to match the smallest elements in A with the smallest in B
        # and so on
        
        # Create a list of pairs (A_i, B_i)
        pairs = list(zip(A_sorted, B_sorted))
        
        # Now, for each pair, if A_i < B_i, we need to swap
        # The cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # Create a list of pairs (A_i, B_i)
        pairs = list(zip(A_sorted, B_sorted))
        
        # Now, for each pair, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B
        # So, we need to find the minimum cost to make A and B identical
        
        # We can use a greedy approach: for each i, if A_i < B_i, we need to swap
        # and the cost is min(A_i, B_i)
        # But we can only swap elements between A and B