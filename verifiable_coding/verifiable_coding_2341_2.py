import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, m, k = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute sorted array for binary search
        sorted_a = sorted(a)
        
        # We need to find the x such that no matter what the others do, we get at least x
        # The best x is the minimum of the possible values we can guarantee
        # We can guarantee the x by choosing the k best elements from the array
        # But we have to ensure that we can take at least one of them in our position
        
        # The number of elements we can choose to control is k
        # We can take the k largest elements and try to ensure that one of them is in our position
        # The answer is the (n - k - 1)th element in the sorted array
        
        # The minimum x we can guarantee is the (n - k - 1)th element in the sorted array
        # Because we can choose to control the first (n - k - 1) elements and ensure that we get the (n - k - 1)th largest element
        x = sorted_a[n - k - 1]
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()