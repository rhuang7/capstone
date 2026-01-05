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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute Grundy numbers for each number
        grundy = []
        for a in A:
            g = 0
            # Compute mex of all possible next states
            next_states = set()
            for divisor in [2, 3, 4, 5, 6]:
                if a % divisor == 0:
                    next_val = a // divisor
                else:
                    next_val = a // divisor
                if next_val == 0:
                    next_states.add(0)
                else:
                    next_states.add(grundy[next_val - 1] if next_val <= 10**18 else 0)
            # Compute mex
            mex = 0
            while mex in next_states:
                mex += 1
            grundy.append(mex)
        
        # XOR all grundy numbers
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        
        if xor_sum != 0:
            results.append("Henry")
        else:
            results.append("Derek")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()