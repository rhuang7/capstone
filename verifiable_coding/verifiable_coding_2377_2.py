import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the sorted version of the array
        sorted_a = sorted(a)
        
        # Find the longest increasing subsequence in the original array that matches the sorted order
        # This subsequence represents elements that are already in the correct relative order
        # The rest of the elements need to be moved, either to the front or the end
        # We can use a greedy approach to find the longest such subsequence
        
        # Create a mapping from value to index in the sorted array
        value_to_index = {val: i for i, val in enumerate(sorted_a)}
        
        # Find the longest subsequence in a that matches the order in sorted_a
        longest = 0
        current = 0
        for val in a:
            if value_to_index[val] >= current:
                current = value_to_index[val] + 1
                longest = max(longest, current)
        
        # The minimum number of operations is n - longest
        results.append(str(n - longest))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()