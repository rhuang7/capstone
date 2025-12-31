import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
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
        
        # Total armrests: each seat (except first and last) has one armrest between them
        # First and last seat in a row have two armrests
        # So total armrests = (M - 2) * N + 2 * N = M * N
        total_armrests = N * M
        
        # Each 'B' uses 2 armrests (both left and right)
        # Each 'L' uses 1 armrest (left)
        # Each 'R' uses 1 armrest (right)
        # 'Z' uses 0 armrests
        
        # Maximum number of B that can be seated is min(B, total_armrests // 2)
        max_B = min(B, total_armrests // 2)
        B_used = min(B, total_armrests // 2)
        remaining_armrests = total_armrests - 2 * B_used
        
        # After using B, we can seat L and R
        # Each L uses 1 armrest (left), each R uses 1 armrest (right)
        # So total armrests used by L and R is L + R
        # But we can only use up to remaining_armrests
        L_used = min(L, remaining_armrests)
        R_used = min(R, remaining_armrests - L_used)
        
        # Total people is Z + L_used + R_used + B_used
        total_people = Z + L_used + R_used + B_used
        results.append(str(total_people))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()