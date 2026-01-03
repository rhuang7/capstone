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
            # The game is equivalent to a Nim heap of size (ni + mi - 2) // 3
            # Because each move can increase the distance by 1, 2, or 3
            # The Grundy number is (ni + mi - 2) // 3
            total += (ni + mi - 2) // 3
        
        if total % 2 == 1:
            results.append("MasterChef")
        else:
            results.append("Football")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()