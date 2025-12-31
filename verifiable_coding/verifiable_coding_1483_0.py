import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    
    caterpillars = list(map(int, data[2:2+K]))
    
    # Set to store damaged leaves
    damaged = set()
    
    for length in caterpillars:
        # The caterpillar starts at position 1
        # It eats leaves at positions 1, 1 + length, 1 + 2*length, ...
        # But must not exceed N
        pos = 1
        while pos <= N:
            damaged.add(pos)
            pos += length
    
    # Count the number of undamaged leaves
    undamaged = N - len(damaged)
    print(undamaged)

if __name__ == '__main__':
    solve()