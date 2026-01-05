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
        N = int(data[idx])
        M = int(data[idx+1])
        Z = int(data[idx+2])
        L = int(data[idx+3])
        R = int(data[idx+4])
        B = int(data[idx+5])
        idx += 6
        
        # Total seats available
        total_seats = N * M
        
        # Total armrests available
        # Each row has (M-1) armrests
        total_armrests = N * (M - 1)
        
        # Each B person uses 2 armrests
        # Each L or R person uses 1 armrest
        # Z people use 0 armrests
        
        # Calculate maximum possible B people
        max_B = min(B, total_armrests // 2)
        remaining_armrests = total_armrests - 2 * max_B
        
        # Calculate maximum possible L and R people
        # Each L or R uses 1 armrest
        # But we can't have more than the remaining armrests
        max_LR = min(L + R, remaining_armrests)
        
        # Calculate maximum possible L and R people considering the remaining armrests
        # We can take as much as possible from L and R
        # But we can't take more than the remaining armrests
        # So take min(L, remaining_armrests) for L and min(R, remaining_armrests - L_taken) for R
        # But since we want to maximize the total, we can take all L and R as long as the sum is <= remaining_armrests
        # So total_LR = min(L + R, remaining_armrests)
        
        # Now, the total number of people is Z + max_B + max_LR
        total_people = Z + max_B + max_LR
        
        results.append(str(total_people))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()