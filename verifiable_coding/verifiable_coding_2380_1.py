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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # We need to find the minimum number of moves to make the string k-periodic
        # A k-periodic string has all 1s at positions i, i + k, i + 2k, ...
        # So we need to find all possible starting positions for 1s and compute the cost
        
        # We'll try all possible starting positions (0 to k-1)
        min_moves = float('inf')
        
        for start in range(k):
            # The positions of 1s in the k-periodic string are start, start + k, start + 2k, ...
            # We need to check if these positions are valid (i.e., < n)
            # We'll count the number of 1s in these positions and compute the cost
            # The cost is the number of 1s not in these positions (we need to flip them to 0)
            # Plus the number of 0s in these positions (we need to flip them to 1)
            # But we also need to make sure that the 1s are in the correct positions
            # So we need to count the number of 1s in these positions and the number of 0s in these positions
            # Then compute the cost as (number of 0s in these positions) + (number of 1s not in these positions)
            
            # Count the number of 1s in the positions start, start + k, ...
            count_ones = 0
            count_zeros = 0
            for i in range(start, n, k):
                if s[i] == '1':
                    count_ones += 1
                else:
                    count_zeros += 1
            
            # The number of 1s not in these positions is (total_ones - count_ones)
            # The number of 0s in these positions is count_zeros
            # So the total cost is (total_ones - count_ones) + count_zeros
            # But we need to make sure that the 1s are in the correct positions
            # So the total cost is (number of 0s in the correct positions) + (number of 1s not in the correct positions)
            # Which is count_zeros + (total_ones - count_ones)
            
            # But we also need to consider that the garland must be k-periodic, so the 1s must be in the correct positions
            # So we need to make sure that the 1s are in the correct positions, and the rest are 0s
            # So the cost is the number of 0s in the correct positions (we need to flip them to 1) plus the number of 1s not in the correct positions (we need to flip them to 0)
            
            # So the cost is count_zeros + (total_ones - count_ones)
            total_ones = s.count('1')
            cost = count_zeros + (total_ones - count_ones)
            if cost < min_moves:
                min_moves = cost
        
        results.append(str(min_moves))
    
    print('\n'.join(results))