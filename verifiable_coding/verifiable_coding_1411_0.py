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
        total_distance = 2 * 3.141592653589793 * R * X
        
        # Time taken for the faster to complete X rounds
        time = total_distance / max(A, B)
        
        # Number of meetings is determined by how many times the faster laps the slower
        # Since they start at the same point, the first meeting is when the faster has lapped the slower
        # So the number of meetings is floor((rel_speed * time) / (2 * pi * R))
        meetings = int((rel_speed * time) // (2 * 3.141592653589793 * R))
        
        # Subtract 1 if the faster is exactly lapping the slower at the end (they meet at the start point)
        if (rel_speed * time) % (2 * 3.141592653589793 * R) == 0:
            meetings -= 1
        
        results.append(meetings)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()