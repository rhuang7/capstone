import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Calculate Grundy numbers for each number
        grundy = []
        for a in A:
            g = 0
            # Compute the Grundy number for a
            # Use memoization to avoid recomputation
            memo = {}
            
            def compute_grundy(x):
                if x == 0:
                    return 0
                if x in memo:
                    return memo[x]
                moves = set()
                for d in [2, 3, 4, 5, 6]:
                    new_x = x // d
                    if new_x == 0:
                        moves.add(0)
                    else:
                        moves.add(compute_grundy(new_x))
                g = 0
                for move in moves:
                    if move == 0:
                        g = 1
                        break
                    if move != 0:
                        g = 1 if move != 0 else 0
                memo[x] = g
                return g
            
            g = compute_grundy(a)
            grundy.append(g)
        
        # XOR all Grundy numbers
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        
        if xor_sum != 0:
            print("Henry")
        else:
            print("Derek")

if __name__ == '__main__':
    solve()