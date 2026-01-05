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
        N = int(data[idx])
        Z1 = int(data[idx+1])
        Z2 = int(data[idx+2])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if either Z1 or Z2 is 0
        # If so, Vanja can win immediately by choosing any element and adding or subtracting it
        if Z1 == 0 or Z2 == 0:
            results.append(1)
            continue
        
        # Check if any element in A can reach Z1 or Z2 in one move
        can_win_first = False
        for a in A:
            if abs(a) == Z1 or abs(a) == Z2:
                can_win_first = True
                break
        if can_win_first:
            results.append(1)
            continue
        
        # Check if any element in A can reach Z1 or Z2 in two moves
        # For two moves, the possible values are:
        # S = a1 + a2, a1 - a2, -a1 + a2, -a1 - a2
        # We need to check if any of these equals Z1 or Z2
        can_win_second = False
        for a in A:
            for b in A:
                if abs(a + b) == Z1 or abs(a - b) == Z1 or abs(-a + b) == Z1 or abs(-a - b) == Z1:
                    can_win_second = True
                    break
                if abs(a + b) == Z2 or abs(a - b) == Z2 or abs(-a + b) == Z2 or abs(-a - b) == Z2:
                    can_win_second = True
                    break
            if can_win_second:
                break
        
        if can_win_second:
            results.append(2)
            continue
        
        # If none of the above, it's a tie
        results.append(0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()