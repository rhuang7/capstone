import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        Z = int(data[index+2])
        L = int(data[index+3])
        R = int(data[index+4])
        B = int(data[index+5])
        index += 6
        
        # Total seats available
        total_seats = N * M
        
        # Total armrests available
        # Each row has (M-1) armrests
        total_armrests = N * (M - 1)
        
        # B people need both armrests, so they take 1 armrest each
        # L people need left armrest, R need right, Z need none
        # We can assign B people first, then L and R
        
        # Maximum possible B people is min(B, total_armrests)
        max_B = min(B, total_armrests)
        B_used = min(B, total_armrests)
        total_armrests -= B_used
        
        # Now assign L and R
        # Each L needs a left armrest, each R needs a right armrest
        # Each seat has one left and one right armrest (except ends)
        # So for each seat, we can have one L and one R
        # But since we have total_armrests, we can assign up to total_armrests people
        # But we have to consider that each person needs one armrest
        
        # For L and R, we can assign up to total_armrests people
        # But we have to consider that each person needs one armrest
        # So the maximum number of people we can assign is min(L + R, total_armrests)
        # But we also have to consider that each person needs one armrest
        
        # However, since L and R can be assigned to different armrests, we can assign up to total_armrests people
        # So the maximum number of people is min(L + R, total_armrests)
        max_LR = min(L + R, total_armrests)
        
        # Now, the total people is Z + max_B + max_LR
        total_people = Z + max_B + max_LR
        results.append(str(total_people))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()