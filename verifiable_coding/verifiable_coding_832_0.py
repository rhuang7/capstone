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
        
        # Sort the array to find the minimum sum subsequence
        A.sort()
        
        # Find the first K elements (they will form the minimum sum)
        min_subseq = A[:K]
        min_sum = sum(min_subseq)
        
        # Count how many times the smallest element appears
        count_min = A.count(min_subseq[0])
        
        # If all elements in the subsequence are the same, the count is combination(N, K)
        if len(set(min_subseq)) == 1:
            from math import comb
            results.append(comb(N, K))
        else:
            # Calculate the number of ways to choose the first element
            first_count = A.count(min_subseq[0])
            # Calculate the number of ways to choose the remaining K-1 elements from the rest
            remaining = A.count(min_subseq[1])
            # If there are multiple elements with the same value as the first, multiply by their combinations
            from math import comb
            total = first_count * comb(remaining, K-1)
            results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()