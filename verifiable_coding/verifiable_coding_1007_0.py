import sys
import math

def compute_gcd_list(arr):
    gcd_list = []
    current_gcd = 0
    for num in arr:
        if current_gcd == 0:
            current_gcd = num
        else:
            current_gcd = math.gcd(current_gcd, num)
        gcd_list.append(current_gcd)
    return gcd_list

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
        max_len = -1
        for i in range(N):
            current_gcd = 0
            for j in range(i, N):
                current_gcd = math.gcd(current_gcd, A[j])
                if current_gcd == 1:
                    max_len = max(max_len, j - i + 1)
        results.append(str(max_len) if max_len != -1 else "-1")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()