import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    K = int(data[1])
    
    lengths = list(map(int, data[2:2+K]))
    
    # Create a set to track damaged leaves
    damaged = set()
    
    for length in lengths:
        # The caterpillar starts at position 1
        # It eats every 'length'th leaf starting from 1
        # So the positions are 1, 1 + length, 1 + 2*length, ...
        # We need to find all such positions <= N
        for i in range(1, N + 1, length):
            damaged.add(i)
    
    # The number of undamaged leaves is N - size of damaged set
    print(N - len(damaged))

if __name__ == '__main__':
    solve()