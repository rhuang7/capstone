import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    
    max_gcd = 0
    max_len = 0
    freq = {}
    
    for num in arr:
        current_gcd = num
        for key in list(freq.keys()):
            current_gcd = math.gcd(current_gcd, key)
            if current_gcd == 0:
                break
        freq[current_gcd] = freq.get(current_gcd, 0) + 1
        if freq[current_gcd] > max_len:
            max_len = freq[current_gcd]
            max_gcd = current_gcd
    
    print(max_len)

if __name__ == '__main__':
    solve()