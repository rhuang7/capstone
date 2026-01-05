import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        x = int(data[index])
        y = int(data[index+1])
        K = int(data[index+2])
        N = int(data[index+3])
        index += 4
        
        # Check if initial positions are same
        if x == y:
            print("Yes")
            continue
        
        # Check if the difference between x and y is divisible by K
        diff = abs(x - y)
        if diff % K != 0:
            print("No")
            continue
        
        # Check if the positions can be made same within the bounds
        # The positions can be made same only if the difference is divisible by 2K
        # Because each move changes the distance by 2K
        if diff % (2 * K) != 0:
            print("No")
            continue
        
        # Check if the positions can be reached within the bounds
        # The maximum distance from the start is N
        # The minimum distance from the start is 0
        # The maximum distance from the end is N
        # The minimum distance from the end is 0
        # The positions can be reached if the distance from the start is <= N and the distance from the end is <= N
        # The distance from the start is abs(x) and from the end is N - x
        # The distance from the start for the thief is abs(y) and from the end is N - y
        # The positions can be reached if the distance from the start is <= N and the distance from the end is <= N
        # But since x and y are already within 0 and N, this is always true
        
        print("Yes")

if __name__ == '__main__':
    solve()