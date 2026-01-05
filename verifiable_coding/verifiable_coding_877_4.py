import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        x = int(data[index])
        y = int(data[index+1])
        K = int(data[index+2])
        N = int(data[index+3])
        index += 4
        
        # If the initial positions are the same, it's already caught
        if x == y:
            results.append("Yes")
            continue
        
        # Calculate the distance between the policeman and the thief
        distance = abs(x - y)
        
        # For the policeman to catch the thief, the distance must be divisible by 2K
        # And the distance must be such that they can meet within the bounds of 0 and N
        if distance % (2 * K) == 0:
            # Check if the meeting point is within the bounds
            meet_pos = x + (distance // (2 * K)) * K
            if 0 <= meet_pos <= N:
                results.append("Yes")
            else:
                results.append("No")
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()