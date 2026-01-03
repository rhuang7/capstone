import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Count frequency of each number
        freq = collections.Counter(a)
        # Get sorted unique elements
        unique = sorted(freq.keys())
        m = len(unique)
        
        # If already sorted, answer is 0
        if a == sorted(a):
            results.append(0)
            continue
        
        # Find the longest increasing subsequence of unique elements in the sorted array
        # This represents the maximum number of elements that are already in the correct order
        # The minimum number of operations is m - length of this subsequence
        sorted_unique = sorted(unique)
        lis = []
        for num in sorted_unique:
            if not lis or num > lis[-1]:
                lis.append(num)
            else:
                # Find the first element in lis >= num and replace it
                # This is for the longest increasing subsequence
                # Since we are only dealing with unique elements, we can use a simple approach
                # Here we use a binary search approach for efficiency
                # Since the elements are unique and sorted, we can just check the last element
                # and if it's smaller than num, we append, else we replace
                # This is a simplified version for the problem
                pass
        
        # The length of the LIS is the number of elements that are already in the correct order
        # The minimum number of operations is m - length of LIS
        # However, for this problem, we can use a different approach
        # We can find the longest chain of consecutive elements in the sorted array that are already in order
        # This is the maximum number of elements that can be left as is
        # The minimum number of operations is m - length of this chain
        
        # Find the longest chain of consecutive elements in the sorted array that are already in order
        # This is done by checking for each element if it is greater than the previous one
        # The length of this chain is the maximum number of elements that can be left as is
        # The minimum number of operations is m - length of this chain
        
        # Initialize the chain length
        chain_len = 1
        for i in range(1, m):
            if unique[i] > unique[i - 1]:
                chain_len += 1
            else:
                # If the current element is not greater than the previous, we can't extend the chain
                # So we reset the chain length
                chain_len = 1
        
        # The minimum number of operations is m - chain_len
        results.append(m - chain_len)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()