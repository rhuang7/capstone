import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        # Since M = N + 1, and Bob starts at a corner and moves along the perimeter
        # The minimum number of moves is calculated based on the perimeter and step size
        perimeter = 4 * N
        M = N + 1
        # The number of moves is the smallest k such that k * M >= perimeter
        # But since Bob can't reverse direction, we need to find the minimum k where k * M >= perimeter
        # However, since Bob starts at a corner and moves along the perimeter, the minimum number of moves is:
        # (perimeter + M - 1) // M
        moves = (perimeter + M - 1) // M
        results.append(str(moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()