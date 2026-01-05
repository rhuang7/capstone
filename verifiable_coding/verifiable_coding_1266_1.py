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
            # Calculate the Grundy number for the board
            # The game is equivalent to a Nim heap with size equal to the number of moves
            # The number of moves is determined by the minimum number of steps to reach (ni, mi)
            # From (1,1) to (ni, mi), the minimum steps is max(ni - 1, mi - 1)
            # But since the allowed moves are combinations of steps, the game is equivalent to a Nim heap of size (ni + mi - 2) // 2
            # This is based on the observation that the game is equivalent to a Nim heap of size (ni + mi - 2) // 2
            # So the Grundy number is (ni + mi - 2) // 2
            grundy = (ni + mi - 2) // 2
            total += grundy
        
        if total % 2 == 1:
            results.append("MasterChef")
        else:
            results.append("Football")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()