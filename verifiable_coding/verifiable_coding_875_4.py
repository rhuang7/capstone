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
        # If so, the first player can choose the element and reach it in one move
        if Z1 == 0 or Z2 == 0:
            results.append(1)
            continue
        
        # Check if there is any element in A that can reach Z1 or Z2 in one move
        can_reach = False
        for a in A:
            if abs(a) == abs(Z1) or abs(a) == abs(Z2):
                can_reach = True
                break
        
        if can_reach:
            results.append(1)
            continue
        
        # Check if there is any element in A that can reach Z1 or Z2 in two moves
        # For two moves, the possible values are:
        # S = a1 + a2, a1 - a2, -a1 + a2, -a1 - a2
        # We need to check if any of these values equals Z1 or Z2
        can_reach_in_two = False
        for a in A:
            for b in A:
                if a + b == Z1 or a + b == Z2 or a - b == Z1 or a - b == Z2 or -a + b == Z1 or -a + b == Z2 or -a - b == Z1 or -a - b == Z2:
                    can_reach_in_two = True
                    break
            if can_reach_in_two:
                break
        
        if can_reach_in_two:
            results.append(2)
            continue
        
        # Check if there is any element in A that can reach Z1 or Z2 in three moves
        # For three moves, the possible values are:
        # S = a1 + a2 + a3, a1 + a2 - a3, a1 - a2 + a3, a1 - a2 - a3, -a1 + a2 + a3, -a1 + a2 - a3, -a1 - a2 + a3, -a1 - a2 - a3
        # We need to check if any of these values equals Z1 or Z2
        can_reach_in_three = False
        for a in A:
            for b in A:
                for c in A:
                    if a + b + c == Z1 or a + b + c == Z2 or a + b - c == Z1 or a + b - c == Z2 or a - b + c == Z1 or a - b + c == Z2 or a - b - c == Z1 or a - b - c == Z2 or -a + b + c == Z1 or -a + b + c == Z2 or -a + b - c == Z1 or -a + b - c == Z2 or -a - b + c == Z1 or -a - b + c == Z2 or -a - b - c == Z1 or -a - b - c == Z2:
                        can_reach_in_three = True
                        break
                if can_reach_in_three:
                    break
            if can_reach_in_three:
                break
        
        if can_reach_in_three:
            results.append(2)
            continue
        
        # Check if there is any element in A that can reach Z1 or Z2 in four moves
        # For four moves, the possible values are:
        # S = a1 + a2 + a3 + a4, a1 + a2 + a3 - a4, a1 + a2 - a3 + a4, a1 + a2 - a3 - a4, a1 - a2 + a3 + a4, a1 - a2 + a3 - a4, a1 - a2 - a3 + a4, a1 - a2 - a3 - a4, -a1 + a2 + a3 + a4, -a1 + a2 + a3 - a4, -a1 + a2 - a3 + a4, -a1 + a2 - a3 - a4, -a1 - a2 + a3 + a4, -a1 - a2 + a3 - a4, -a1 - a2 - a3 + a4, -a1 - a2 - a3 - a4
        # We need to check if any of these values equals Z1 or Z2
        can_reach_in_four = False
        for a in A:
            for b in A:
                for c in A:
                    for d in A:
                        if a + b + c + d == Z1 or a + b + c + d == Z2 or a + b + c - d == Z1 or a + b + c - d == Z2 or a + b - c + d == Z1 or a + b - c + d == Z2 or a + b - c - d == Z1 or a + b - c - d == Z2 or a - b + c + d == Z1 or a - b + c + d == Z2 or a - b + c - d == Z1 or a - b + c - d == Z2 or a - b - c + d == Z1 or a - b - c + d == Z2 or a - b - c - d == Z1 or a - b - c - d == Z2 or -a + b + c + d == Z1 or -a + b + c + d == Z2 or -a + b + c - d == Z1 or -a + b + c - d == Z2 or -a + b - c + d == Z1 or -a + b - c + d == Z2 or -a + b - c - d == Z1 or -a + b - c - d == Z2 or -a - b + c + d == Z1 or -a - b + c + d == Z2 or -a - b + c - d == Z1 or -a - b + c - d == Z2 or -a - b - c + d == Z1 or -a - b - c + d == Z2 or -a - b - c - d == Z1 or -a - b - c - d == Z2:
                            can_reach_in_four = True
                            break
                        if can_reach_in_four:
                            break
                    if can_reach_in_four:
                        break
                if can_reach_in_four:
                    break
            if can_reach_in_four:
                break
        
        if can_reach_in_four:
            results.append(2)
            continue
        
        # Check if there is any element in A that can reach Z1 or Z2 in five moves
        # For five moves, the possible values are:
        # S = a1 + a2 + a3 + a4 + a5, a1 + a2 + a3 + a4 - a5, a1 + a2 + a3 - a4 + a5, a1 + a2 + a3 - a4 - a5, a1 + a2 - a3 + a4 + a5, a1 + a2 - a3 + a4 - a5, a1 + a2 - a3 - a4 + a5, a1 + a2 - a3 - a4 - a5, a1 - a2 + a3 + a4 + a5, a1 - a2 + a3 + a4 - a5, a1 - a2 + a3 - a4 + a5, a1 - a2 + a3 - a4 - a5, a1 - a2 - a3 + a4 + a5, a1 - a2 - a3 + a4 - a5, a1 - a2 - a3 - a4 + a5, a1 - a2 - a3 - a4 - a5, -a1 + a2 + a3 + a4 + a5, -a1 + a2 + a3 + a4 - a5, -a1 + a2 + a3 - a4 + a5, -a1 + a2 + a3 - a4 - a5, -a1 + a2 - a3 + a4 + a5, -a1 + a2 - a3 + a4 - a5, -a1 + a2 - a3 - a4 + a5, -a1 + a2 - a3 - a4 - a5, -a1 - a2 + a3 + a4 + a5, -a1 - a2 + a3 + a4 - a5, -a1 - a2 + a3 - a4 + a5, -a1 - a2 +