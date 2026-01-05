import sys

def solve():
    input = sys.stdin.buffer.read().split()
    N = int(input[0])
    idx = 1
    for _ in range(N):
        G = int(input[idx])
        T = int(input[idx+1])
        W = int(input[idx+2])
        idx += 3
        
        # Sort the counts
        a, b, c = sorted([G, T, W])
        
        # Check if the largest count is <= sum of the other two
        if a <= b + c:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()