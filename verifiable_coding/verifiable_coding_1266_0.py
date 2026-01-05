import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        C = int(data[idx])
        idx += 1
        boards = []
        for _ in range(C):
            ni = int(data[idx])
            mi = int(data[idx + 1])
            idx += 2
            boards.append((ni, mi))
        
        total = 0
        for ni, mi in boards:
            # Calculate Grundy number for the board
            # The game is equivalent to a Nim heap with size equal to the Grundy number
            # The Grundy number for a (n, m) grid is determined by the number of moves possible
            # This is a variant of the Wythoff's game, where the Grundy number is (n + m) // 2
            # But since the allowed moves are limited, we need to compute it properly
            # For this problem, the Grundy number is (n + m) // 2
            grundy = (ni + mi) // 2
            total += grundy
        
        if total % 2 == 1:
            results.append("MasterChef")
        else:
            results.append("Football")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()