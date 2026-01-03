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
        
        # Check if initial positions are same
        if x == y:
            results.append("Yes")
            continue
        
        # Calculate the distance between x and y
        dist = abs(x - y)
        
        # Check if the distance is divisible by 2K
        if dist % (2 * K) != 0:
            results.append("No")
            continue
        
        # Check if the positions can reach the same point
        # The thief and policeman can only meet if their positions are congruent modulo 2K
        if (x % (2 * K)) == (y % (2 * K)):
            results.append("Yes")
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()