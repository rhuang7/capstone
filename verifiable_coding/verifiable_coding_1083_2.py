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
        total_people = Z + L + R + B
        
        # Calculate maximum possible people
        # Each seat can accommodate at most 1 person
        max_people = min(total_people, total_seats)
        results.append(str(max_people))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()