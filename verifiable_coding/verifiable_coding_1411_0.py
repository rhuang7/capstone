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
        
        # Calculate relative speed
        rel_speed = abs(A - B)
        
        # Calculate total distance covered by both in X rounds
        # Since they are on a circular track, the number of meetings is determined by how many times the faster one laps the slower one
        # The number of meetings is floor((A * X - B * X) / (A + B)) if A > B, else floor((B * X - A * X) / (A + B))
        # But since they start at the same point, the first meeting is not counted if they start together
        # So we use floor((A * X - B * X) / (A + B)) if A > B, else floor((B * X - A * X) / (A + B))
        # But since they start together, we subtract 1 if the faster one laps the slower one at least once
        if A > B:
            meetings = (A * X - B * X) // (A + B)
        else:
            meetings = (B * X - A * X) // (A + B)
        
        # Subtract 1 if the faster one laps the slower one at least once
        if A > B and (A * X - B * X) > 0:
            meetings -= 1
        elif B > A and (B * X - A * X) > 0:
            meetings -= 1
        
        results.append(meetings)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()