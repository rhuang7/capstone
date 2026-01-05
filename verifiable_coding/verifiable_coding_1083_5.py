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
        # Each seat (except first and last) has 1 armrest between them
        # First and last seat have 2 armrests each
        armrests = (N * (M - 2)) + 2 * N
        
        # Calculate maximum possible people
        # B people need both armrests, so they take 2 armrests each
        # L people need left armrest, R need right, Z need none
        # We need to maximize the number of people that can be seated
        
        # First, allocate B people
        # Each B person uses 2 armrests
        max_B = min(B, armrests // 2)
        remaining_armrests = armrests - 2 * max_B
        B_used = min(B, max_B)
        B_remaining = B - B_used
        
        # Now allocate L and R people
        # Each L needs 1 armrest (left)
        # Each R needs 1 armrest (right)
        # We can only allocate as many as possible without exceeding remaining armrests
        
        # The total armrests used by L and R is L + R
        # But we can only use up to remaining_armrests
        total_L_R = L + R
        max_L_R = min(total_L_R, remaining_armrests)
        
        # Now, allocate Z people
        # Z people don't need any armrests
        # So they can be allocated as long as there are seats left
        
        # Total people = B_used + max_L_R + Z_used
        # But we also need to make sure that the total people doesn't exceed total_seats
        
        # Calculate total people
        total_people = B_used + max_L_R + Z
        
        # But we also have to make sure that the total people doesn't exceed the total seats
        total_people = min(total_people, total_seats)
        
        results.append(str(total_people))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()