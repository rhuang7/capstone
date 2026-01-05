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
            # Calculate the number of moves possible on the board
            # The game is similar to a Nim game where each board contributes a pile of stones
            # The number of moves is (ni * mi) - 1, but we need to find the Grundy number
            # For this problem, the Grundy number for a board of size (n, m) is (n * m) % 2
            # If the total XOR of all Grundy numbers is non-zero, Chef wins; else, brother wins
            total ^= (ni * mi) % 2
        
        if total != 0:
            results.append("MasterChef")
        else:
            results.append("Football")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()