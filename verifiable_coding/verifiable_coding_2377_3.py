import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Sort the array to find the target order
        sorted_a = sorted(a)
        
        # Find the longest increasing subsequence that is already in order
        # This subsequence will be the part that doesn't need to be moved
        # The rest of the elements need to be moved
        # We use a dynamic programming approach to find the length of the longest increasing subsequence
        # Since all elements are distinct, we can use a simple approach
        
        # Create a list of indices of elements in the sorted array
        pos = {val: i for i, val in enumerate(sorted_a)}
        
        # Find the length of the longest increasing subsequence in the original array
        # that matches the order in the sorted array
        l = 0
        for val in a:
            if pos[val] > l:
                l = pos[val]
        
        # The minimum number of operations is n - l
        print(n - l)

if __name__ == '__main__':
    solve()