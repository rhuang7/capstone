import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    lengths = list(map(int, data[2:2+K]))
    
    # Initialize a set to keep track of damaged leaves
    damaged = set()
    
    for l in lengths:
        # The caterpillar starts at position 1
        # It eats every l-th leaf starting from 1
        # So the positions are 1, 1+l, 1+2l, ... until <= N
        pos = 1
        while pos <= N:
            damaged.add(pos)
            pos += l
    
    # The number of undamaged leaves is N minus the size of the damaged set
    print(N - len(damaged))

if __name__ == '__main__':
    solve()