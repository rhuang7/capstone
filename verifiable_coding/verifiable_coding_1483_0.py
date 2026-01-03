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
        # It eats leaves at positions 1, 1 + l, 1 + 2*l, ...
        # So the positions are 1 + i*l for i >= 0
        # We need to find all such positions <= N
        i = 0
        while True:
            pos = 1 + i * l
            if pos > N:
                break
            damaged.add(pos)
            i += 1
    
    # The total number of leaves is N
    # The number of undamaged leaves is N - size of damaged set
    print(N - len(damaged))

if __name__ == '__main__':
    solve()