import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        X = int(data[index])
        R = int(data[index+1])
        A = int(data[index+2])
        B = int(data[index+3])
        index += 4
        
        # Calculate the relative speed
        rel_speed = abs(A - B)
        
        # Total distance covered by both in X rounds
        total_distance = X * 2 * 3.141592653589793 * R
        
        # Time taken to complete X rounds by the slower runner
        time = total_distance / min(A, B)
        
        # Number of meetings is the total distance covered by the faster runner
        # divided by the circumference, but only if the faster runner is faster
        if A > B:
            meetings = (A * time) // (2 * 3.141592653589793 * R)
        else:
            meetings = (B * time) // (2 * 3.141592653589793 * R)
        
        results.append(str(meetings))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()