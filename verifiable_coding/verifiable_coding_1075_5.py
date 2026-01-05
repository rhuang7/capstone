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
        for num in A:
            g = 0
            for d in [2, 3, 4, 5, 6]:
                if num % d == 0:
                    next_num = num // d
                    if next_num == 0:
                        g = 1
                    else:
                        g ^= grundy_next[next_num]
            grundy.append(g)
        
        # Compute XOR of all Grundy numbers
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