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
        
        total_seats = N * M
        total_armrests = (N * (M - 1)) + (2 * N)  # M-1 between seats, 2 at ends
        
        # Calculate available armrests for B
        available_for_B = min(B, total_armrests)
        B_used = available_for_B
        B_remaining = B - B_used
        
        # Calculate available armrests for L and R
        available_for_L = min(L, (total_armrests - B_used) // 2)
        available_for_R = min(R, (total_armrests - B_used) // 2)
        
        # Calculate total people
        total = Z + L + R + B_used
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()