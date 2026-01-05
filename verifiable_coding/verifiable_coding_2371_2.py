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
        
        # We need to find the minimal k such that the subarray a[k:] is good
        # A subarray is good if we can arrange it into a non-decreasing array by taking elements from either end
        
        # We can use a greedy approach: try to find the minimal k such that the subarray a[k:] is good
        # We can use a two-pointer approach to check if a subarray is good
        
        # Function to check if a subarray is good
        def is_good(sub):
            left = 0
            right = len(sub) - 1
            c = []
            while left <= right:
                if not c or sub[left] <= c[-1]:
                    c.append(sub[left])
                    left += 1
                elif not c or sub[right] <= c[-1]:
                    c.append(sub[right])
                    right -= 1
                else:
                    return False
            return True
        
        # Try all possible k from 0 to n
        for k in range(n+1):
            if is_good(a[k:]):
                results.append(str(k))
                break
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()