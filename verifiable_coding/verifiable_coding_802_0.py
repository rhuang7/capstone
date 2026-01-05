import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        C = int(data[index+2])
        index += 3
        
        # Convert to binary strings
        bin_A = bin(A)[2:]
        bin_B = bin(B)[2:]
        bin_C = bin(C)[2:]
        
        # Pad with leading zeros to make them the same length
        max_len = max(len(bin_A), len(bin_B), len(bin_C))
        bin_A = bin_A.zfill(max_len)
        bin_B = bin_B.zfill(max_len)
        bin_C = bin_C.zfill(max_len)
        
        # Count the number of 1s in each binary string
        cnt_A = bin_A.count('1')
        cnt_B = bin_B.count('1')
        cnt_C = bin_C.count('1')
        
        # If the number of 1s in C is not equal to the sum of 1s in A and B, it's impossible
        if cnt_C != cnt_A + cnt_B:
            results.append(0)
            continue
        
        # Count the number of 1s in each position
        cnt_1 = 0
        cnt_0 = 0
        for a, b, c in zip(bin_A, bin_B, bin_C):
            if a == '1' and b == '1' and c == '1':
                cnt_1 += 1
            elif a == '1' or b == '1':
                cnt_0 += 1
        
        # The number of ways is the number of ways to choose positions for 1s in A and B
        # such that the sum of 1s in each position matches C
        # This is a combinatorial problem: choose cnt_1 positions for 1s in A and B
        # and the rest are 0s
        # The number of ways is C(cnt_0 + cnt_1, cnt_1)
        from math import comb
        results.append(comb(cnt_0 + cnt_1, cnt_1))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()