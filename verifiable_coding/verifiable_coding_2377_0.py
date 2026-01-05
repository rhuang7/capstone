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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array to find the target order
        sorted_a = sorted(a)
        
        # Find the longest increasing subsequence in the original array that is in the sorted order
        # This subsequence represents elements that are already in the correct relative order
        # The number of operations needed is n - length of this subsequence
        
        # Create a mapping from value to index in the sorted array
        value_to_index = {val: i for i, val in enumerate(sorted_a)}
        
        # Find the length of the longest increasing subsequence in the original array
        # where each element's index in the sorted array is increasing
        l = 0
        for val in a:
            i = value_to_index[val]
            if i > l:
                l = i
        
        results.append(n - l)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()