import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    lengths = list(map(int, data[2:2+K]))
    
    # Set to store damaged leaves
    damaged = set()
    
    for l in lengths:
        # The caterpillar starts at position 1
        # It eats every l-th leaf starting from 1
        # So the positions are 1, 1+l, 1+2l, ...
        # We need to find all such positions <= N
        for i in range(1, N // l + 1):
            pos = 1 + (i - 1) * l
            damaged.add(pos)
    
    # The total number of leaves is N
    # The number of undamaged leaves is N - size of damaged set
    print(N - len(damaged))

if __name__ == '__main__':
    solve()