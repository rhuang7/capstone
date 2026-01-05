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
        
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        
        # Check if the combined sorted list can be split into two equal parts
        combined = sorted(A + B)
        if len(combined) % 2 != 0:
            results.append(-1)
            continue
        
        # Check if the combined list can be split into two equal parts
        if combined[:N] != A_sorted or combined[N:] != B_sorted:
            results.append(-1)
            continue
        
        # Now find the minimum cost
        # We need to pair elements from A and B such that each element in A is matched with an element in B
        # The cost is min(A_i, B_j) for each swap
        # We can use a greedy approach: sort A and B, then pair them in a way that minimizes the cost
        
        # Sort A and B
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        
        # Pair A[i] with B[i] and calculate the cost
        cost = 0
        for i in range(N):
            if A_sorted[i] != B_sorted[i]:
                # We need to swap A[i] with B[j] such that after swapping, A[i] and B[j] are in their correct positions
                # Find the smallest j where B[j] > A[i]
                # This is the minimal cost to fix this position
                # We can use a greedy approach here
                # Find the first B[j] that is larger than A[i]
                # Since B is sorted, we can use binary search
                # But for simplicity, we can just iterate from the end
                # This is O(N^2) in worst case, but with N up to 2e5, this is not feasible
                # So we need a better approach
                
                # We can use a two-pointer approach
                # Let's try to pair A[i] with B[j] such that A[i] <= B[j]
                # We can use a two-pointer approach
                # Initialize pointers
                i_a = i
                i_b = N - 1
                
                while i_a < N and i_b >= 0:
                    if A_sorted[i_a] <= B_sorted[i_b]:
                        # We can swap A[i_a] with B[i_b]
                        cost += min(A_sorted[i_a], B_sorted[i_b])
                        i_a += 1
                        i_b -= 1
                    else:
                        i_b -= 1
                
                if i_a >= N:
                    results.append(-1)
                    break
        else:
            results.append(cost)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()