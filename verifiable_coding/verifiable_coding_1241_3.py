import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        total = sum(A)
        remaining = N - X
        
        # Calculate the sum of the remaining piles
        # Since all piles are removed in X moves, the remaining piles are N - X
        # We need to choose which piles to remove such that the sum of the remaining is odd or even
        
        # To determine the parity of the sum of remaining piles, we need to consider:
        # The total sum of all piles, and how many piles are removed (X)
        # The sum of the remaining piles is total - sum(removed_piles)
        # We need to find if it's possible to remove X piles such that the sum of the remaining is odd or even
        
        # The parity of the sum of the remaining piles depends on the parity of the total sum and the parity of the sum of the removed piles
        # So, we need to find if there exists a way to remove X piles such that the sum of the removed piles has the opposite parity of the total sum
        
        # So, we need to check if there are at least X piles with even sum or odd sum, depending on the parity of the total sum
        
        # Count the number of even and odd elements
        even_count = 0
        odd_count = 0
        for num in A:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # Total sum parity
        total_parity = total % 2
        
        # We need to remove X piles such that the sum of removed piles has the opposite parity of total_parity
        # So, we need to check if there are enough even or odd piles to achieve this
        
        # If total_parity is 0 (even), we need to remove X piles with odd sum (so that total - odd = even - odd = odd)
        # If total_parity is 1 (odd), we need to remove X piles with even sum (so that total - even = odd - even = odd)
        
        # So, check if there are enough piles of the required parity to remove X of them
        
        if total_parity == 0:
            # Need to remove X odd piles
            if odd_count >= X:
                results.append("Walter")
            else:
                results.append("Jesse")
        else:
            # Need to remove X even piles
            if even_count >= X:
                results.append("Walter")
            else:
                results.append("Jesse")
    
    print('\n'.join(results))