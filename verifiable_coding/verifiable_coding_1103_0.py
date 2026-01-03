import sys
import math

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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        freq = {}
        for num in a:
            temp = num
            for i in range(2, int(math.isqrt(temp)) + 1):
                if temp % i == 0:
                    count = 0
                    while temp % i == 0:
                        temp //= i
                        count += 1
                    if count >= 2:
                        freq[i] = 1
                        break
            if temp > 1:
                freq[temp] = 1
        
        for p in freq:
            print(p)
            break

if __name__ == '__main__':
    solve()