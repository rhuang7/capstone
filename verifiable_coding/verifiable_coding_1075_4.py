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
            # We need to find the mex of all possible moves
            # A move is to divide by 2, 3, 4, 5, 6 and take floor
            # If the result is 0, it is removed, so it's like a move to 0
            # So for each possible move, we compute the grundy number of the new value
            # and collect them in a set, then mex is the smallest non-negative integer not in the set
            reachable = set()
            for divisor in [2, 3, 4, 5, 6]:
                new_val = a // divisor
                if new_val > 0:
                    reachable.add(grundy_new(new_val))
                else:
                    reachable.add(0)
            # Compute mex
            mex = 0
            while mex in reachable:
                mex += 1
            grundy.append(mex)
        
        # The total game is the XOR of all grundy numbers
        total_xor = 0
        for g in grundy:
            total_xor ^= g
        
        if total_xor != 0:
            print("Henry")
        else:
            print("Derek")

def grundy_new(a):
    if a == 0:
        return 0
    g = 0
    reachable = set()
    for divisor in [2, 3, 4, 5, 6]:
        new_val = a // divisor
        if new_val > 0:
            reachable.add(grundy_new(new_val))
        else:
            reachable.add(0)
    mex = 0
    while mex in reachable:
        mex += 1
    return mex

if __name__ == '__main__':
    solve()