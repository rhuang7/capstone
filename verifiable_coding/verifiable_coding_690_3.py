import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    M = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    if any(a == 0 for a in A):
        print(-1)
        return
    
    # We need to find the minimum number of speeches such that
    # for every consecutive K soldiers, the sum is >= M
    # Each speech multiplies a contiguous K soldiers' morale by X (X > 1)
    
    # We can use a greedy approach: always choose the leftmost window that needs a speech
    # and multiply the entire window by X (X is chosen such that the sum is >= M)
    
    # We'll use a sliding window approach to find the minimum number of speeches
    
    # We'll use a binary search approach to find the minimum number of speeches
    # Let's binary search on the number of speeches
    low = 0
    high = N  # Maximum possible speeches is N (each soldier can be in a speech)
    
    answer = -1
    
    while low <= high:
        mid = (low + high) // 2
        # Check if it's possible to give mid speeches
        # We'll use a greedy approach to assign speeches
        # We'll try to assign speeches to the leftmost possible window
        # and multiply the entire window by X (X is chosen such that the sum is >= M)
        
        # We'll need to track the current morale of each soldier
        # and the current sum of each window
        # We'll use a sliding window approach to find the minimum number of speeches
        
        # Initialize the current morale array
        current = A[:]
        # Initialize the number of speeches
        speeches = 0
        
        # We'll use a sliding window to check if it's possible to give mid speeches
        # We'll use a greedy approach to assign speeches to the leftmost possible window
        # and multiply the entire window by X (X is chosen such that the sum is >= M)
        
        i = 0
        while i < N:
            # Check if the current window of K soldiers has sum < M
            # If so, we need to give a speech to this window
            # We'll multiply the entire window by X (X is chosen such that the sum is >= M)
            # We'll find X such that (sum * X) >= M
            # X = ceil(M / sum)
            # But since X must be > 1, we need to ensure that sum * X >= M and X > 1
            # So X = ceil(M / sum)
            # If sum == 0, it's impossible (but we already checked that all A[i] are > 0)
            window_sum = sum(current[i:i+K])
            if window_sum < M:
                # Need to give a speech to this window
                # Find X such that (window_sum * X) >= M and X > 1
                X = (M + window_sum - 1) // window_sum
                if X <= 1:
                    # Not possible to increase the sum
                    break
                # Multiply the entire window by X
                for j in range(i, i+K):
                    current[j] *= X
                speeches += 1
                if speeches > mid:
                    break
            i += 1
        
        if speeches <= mid:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    print(answer)

if __name__ == '__main__':
    solve()