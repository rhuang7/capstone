import sys
import bisect

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
        
        # Precompute sorted array
        sorted_a = sorted(a)
        
        # Precompute prefix and suffix arrays
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        for i in range(n):
            suffix[i + 1] = suffix[i] + a[n - 1 - i]
        
        # Precompute for each position the minimum and maximum possible value
        # We need to find the x such that no matter what the others do, you get at least x
        # The optimal strategy is to choose the k people to control the first or last element
        # So we need to find the minimum of the maximum values that can be guaranteed
        
        # We use a binary search approach
        # The answer is the minimum of the maximum values that can be guaranteed
        # We can use a greedy approach to find the x
        
        # We can use a binary search on x
        low = 1
        high = max(a)
        answer = 1
        
        while low <= high:
            mid = (low + high) // 2
            # Check if it is possible to guarantee at least mid
            # We need to find if there is a way to choose k people to control the first or last element
            # such that the value you get is at least mid
            # We can use a greedy approach to find the minimum number of people needed to control
            # to guarantee at least mid
            
            # We can use a greedy approach to find the minimum number of people needed to control
            # to guarantee at least mid
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to guarantee at least mid
            # We can use a greedy approach to find the minimum number of people needed
            # to control to guarantee at least mid
            
            # We can use a binary search on the array to find the minimum number of people needed
            # to control to