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
            # The game is equivalent to a Nim heap with size equal to the Grundy number
            # The Grundy number for a (ni, mi) board can be computed as follows:
            # If ni == mi, the Grundy number is (ni - 1) // 2
            # Otherwise, the Grundy number is (min(ni, mi) - 1) // 2
            g = (min(ni, mi) - 1) // 2
            total += g
        
        if total % 2 == 1:
            results.append("MasterChef")
        else:
            results.append("Football")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()