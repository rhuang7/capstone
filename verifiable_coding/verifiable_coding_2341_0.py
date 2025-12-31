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
        # The optimal strategy is to choose the k people to control the first or last element
        # We need to find the minimum value that can be guaranteed in the worst case
        
        # The answer is the (n - k - 1)-th smallest element in the array
        # Because we can control k people, so we can ensure that the remaining (n - k - 1) elements are chosen by others
        # The worst case is that the others choose the smallest (n - k - 1) elements
        # So the answer is the (n - k - 1)-th smallest element
        
        # But we also have to consider the position m
        # The person at position m will get the element at the (m-1)-th step of the process
        # However, the exact element depends on the choices made by others
        # The optimal strategy is to choose the k people to control the first or last element
        # So the answer is the (n - k - 1)-th smallest element in the array
        
        x = sorted_a[n - k - 1]
        results.append(str(x))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()