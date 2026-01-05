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
        relative_speed = abs(A - B)
        
        # Calculate the number of meetings
        # Each meeting happens every 1/(relative_speed) rounds
        # But since they start at the same point, the first meeting is after 1/(relative_speed) rounds
        # So the total number of meetings is floor((X - 1) * relative_speed)
        meetings = (X - 1) * relative_speed
        
        results.append(str(meetings))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()