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
        
        # Sort both arrays
        A_sorted = sorted(A)
        B_sorted = sorted(B)
        
        # Check if the sorted arrays can be made identical
        for i in range(N):
            if A_sorted[i] != B_sorted[i]:
                results.append("-1")
                break
        else:
            # Calculate the minimum cost
            # We need to pair elements from A and B such that each element in A is paired with an element in B
            # The cost is min(A_i, B_j) for each swap
            # To minimize the total cost, we should pair the smallest elements with the smallest elements
            # So we sort A and B, then pair them and sum the min of each pair
            A_sorted = sorted(A)
            B_sorted = sorted(B)
            total_cost = 0
            for a, b in zip(A_sorted, B_sorted):
                total_cost += min(a, b)
            results.append(str(total_cost))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()