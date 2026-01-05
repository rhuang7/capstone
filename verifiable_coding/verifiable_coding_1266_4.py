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
            # The game is equivalent to a Nim heap of size (ni + mi - 2) // 2
            # Because the maximum number of moves is (ni + mi - 2) // 2
            # Each move reduces the distance from (1,1) to (ni,mi)
            # The Grundy number is the same as the number of moves
            moves = (ni + mi - 2) // 2
            total += moves
        
        if total % 2 == 1:
            results.append("MasterChef")
        else:
            results.append("Football")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()