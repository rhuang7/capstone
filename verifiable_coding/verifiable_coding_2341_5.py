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
        n, m, k = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute sorted array for binary search
        sorted_a = sorted(a)
        
        # We need to find the x such that no matter what the others do, we get at least x
        # The optimal strategy is to control the first k people in the line
        # So we can choose the best k elements from the array to guarantee at least x
        
        # The maximum x is the (n - k)th smallest element in the array
        # Because we can choose the best k elements to be controlled, and the remaining (n - k) elements are the worst case
        # So the answer is the (n - k)th smallest element in the array
        # But we have to make sure that we are in position m, so we need to find the (n - k)th smallest element in the array
        # But wait, the position m is important. We need to find the x such that no matter what the others do, we get at least x
        # The worst case is that the other people take the worst possible elements, so we need to find the x such that there are at least (n - m) elements >= x
        # So the answer is the (n - m - k)th smallest element in the array
        
        # However, the correct way is to find the x such that there are at least (n - m) elements >= x, and we can choose k elements to be controlled
        # So the answer is the (n - m - k)th smallest element in the array
        
        # So the answer is the (n - m - k)th smallest element in the array
        # But if n - m - k < 0, then x is the minimum element in the array
        # Because we can choose k people to control, and the rest will take the worst possible elements, but we are in position m, so we can take the best possible element
        
        # So the answer is the (n - m - k)th smallest element in the array, or the minimum if n - m - k < 0
        
        if n - m - k < 0:
            x = min(a)
        else:
            x = sorted_a[n - m - k]
        
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()