import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Find the sorted version of the array
        sorted_a = sorted(a)
        
        # Find the longest subsequence of elements in a that are in the same order as in sorted_a
        # This subsequence will be the elements that do not need to be moved
        longest = 0
        for i in range(n):
            if a[i] == sorted_a[i]:
                longest += 1
            else:
                break
        
        # Check for the rest of the elements
        for i in range(n - 1, -1, -1):
            if a[i] == sorted_a[i]:
                longest += 1
            else:
                break
        
        # The minimum number of operations is n - longest
        print(n - longest)

if __name__ == '__main__':
    solve()