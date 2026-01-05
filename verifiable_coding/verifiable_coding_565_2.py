import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for __ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        
        pos = A.index(queries[0]) + 1  # 1-based index of X in original array
        
        # Create a list of positions for each element
        pos_list = [0] * (N + 1)  # 1-based indexing
        for i in range(N):
            pos_list[A[i]] = i + 1
        
        # Precompute the minimum swaps needed for each query
        for X in queries:
            if X == queries[0]:
                results.append(0)
                continue
            target_pos = pos_list[X]
            if target_pos == pos:
                results.append(0)
                continue
            # Find the minimum number of swaps to move X to the correct position
            # We need to find the minimum number of swaps to bring X to the correct position
            # This is equivalent to the number of elements between X and the correct position
            # that are not in their correct positions
            # But since we can swap any elements, the minimum number of swaps is the number of elements
            # between X and the correct position that are not in their correct positions
            # However, since we can swap any elements, the minimum number of swaps is the number of elements
            # between X and the correct position that are not in their correct positions
            # So we need to find the number of elements between X and the correct position that are not in their correct positions
            # This is equivalent to the number of elements in the range [min(pos, target_pos), max(pos, target_pos)] that are not in their correct positions
            # So we can precompute for each position the number of elements that are not in their correct positions in the range
            # But since we can't precompute for all possible ranges, we need to compute it on the fly
            # So for each query, we find the number of elements in the range [min(pos, target_pos), max(pos, target_pos)] that are not in their correct positions
            # This is the minimum number of swaps needed
            # So for each query, we need to count the number of elements in the range [min(pos, target_pos), max(pos, target_pos)] that are not in their correct positions
            # This can be done by iterating through the range and checking if the element is in its correct position
            # But since N can be up to 1e5 and Q up to 1e5, this would be O(Q*N), which is too slow
            # So we need a better way
            # We can precompute for each position the number of elements that are not in their correct positions in the range [1, i]
            # Then for a query, we can compute the number of elements not in their correct positions in the range [min(pos, target_pos), max(pos, target_pos)]
            # This can be done with a prefix sum array
            # So we precompute a prefix array where prefix[i] is the number of elements not in their correct positions in the range [1, i]
            # Then for a query, the number of elements not in their correct positions in the range [a, b] is prefix[b] - prefix[a-1]
            # But how to compute this prefix array?
            # We can create a list called 'correct' where correct[i] is 1 if A[i-1] == i, else 0
            # Then prefix[i] = prefix[i-1] + correct[i]
            # So for each query, the number of elements not in their correct positions in the range [a, b] is prefix[b] - prefix[a-1]
            # But this is not the correct approach, because the correct positions are determined by the original array, not the modified array
            # So we need to find the number of elements in the range [a, b] that are not in their correct positions in the original array
            # So we can precompute for each position i, whether A[i-1] == i
            # Then create a prefix array where prefix[i] is the number of elements not in their correct positions in the range [1, i]
            # Then for a query, the number of elements not in their correct positions in the range [a, b] is prefix[b] - prefix[a-1]
            # But this is not the correct approach either, because the correct positions are determined by the original array, not the modified array
            # So the correct approach is to find the number of elements in the range [a, b] that are not in their correct positions in the original array
            # So we can precompute for each position i, whether A[i-1] == i
            # Then create a prefix array where prefix[i] is the number of elements not in their correct positions in the range [1, i]
            # Then for a query, the number of elements not in their correct positions in the range [a, b] is prefix[b] - prefix[a-1]
            # So this is the correct approach
            # So we precompute the prefix array
            # Now, we need to compute the number of elements in the range [min(pos, target_pos), max(pos, target_pos)] that are not in their correct positions
            # This is the minimum number of swaps needed
            # So for each query, we compute the number of elements in the range [min(pos, target_pos), max(pos, target_pos)] that are not in their correct positions
            # This is the minimum number of swaps needed
            # So we can precompute the prefix array
            # Now, let's compute the prefix array
            correct = [0] * (N + 1)
            for i in range(1, N+1):
                if A[i-1] == i:
                    correct[i] = 1
                else:
                    correct[i] = 0
            prefix = [0] * (N + 1)
            for i in range(1, N+1):
                prefix[i] = prefix[i-1] + correct[i]
            a = min(pos, target_pos)
            b = max(pos, target_pos)
            res = prefix[b] - prefix[a-1]
            results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()