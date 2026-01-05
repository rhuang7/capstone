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
        
        # Compute Grundy numbers for each number
        grundy = []
        for a in A:
            g = 0
            for d in [2, 3, 4, 5, 6]:
                if a % d == 0:
                    next_val = a // d
                    if next_val == 0:
                        continue
                    g = max(g, grundy[next_val - 1])
            grundy.append(g)
        
        # XOR all grundy numbers
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        
        if xor_sum != 0:
            print("Henry")
        else:
            print("Derek")

if __name__ == '__main__':
    solve()