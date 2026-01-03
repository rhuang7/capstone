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
        
        # Total people that can be seated
        # Each seat can be occupied by one person
        max_people = total_seats
        
        # B people need both armrests, so they take one seat
        # L people need left armrest, R need right
        # Z need none
        # We can seat all Z, L, R, B people as long as they fit in the seats
        # But we need to make sure that the number of people that need armrests
        # does not exceed the available armrests
        
        # Calculate the number of armrests available
        # Each seat has 1 armrest between two seats, and 2 at the ends
        # So total armrests per row is M + 1
        # Total armrests in the cinema: N * (M + 1)
        total_armrests = N * (M + 1)
        
        # B people need 2 armrests each
        # L and R need 1 each
        # Z need 0
        # So total armrests needed is 2*B + L + R
        required_armrests = 2 * B + L + R
        
        # The maximum number of people is the minimum of:
        # - total_seats (since each person needs one seat)
        # - total_armrests (since each person needs armrests)
        # - Z + L + R + B (total people)
        # But we also have to consider that some people may not fit into the armrests
        # So the answer is the minimum of these three values
        max_people = min(total_seats, total_armrests, Z + L + R + B)
        
        results.append(str(max_people))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()