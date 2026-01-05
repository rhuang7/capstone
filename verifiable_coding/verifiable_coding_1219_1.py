import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        
        # Calculate the product of M^i for i in 1..N
        # But since N can be up to 1e9, we need to compute it efficiently using modular exponentiation
        # However, since M can be up to 1e14, we need to compute M^N mod MOD
        # But since N can be up to 1e9, we need to compute pow(M, N, MOD)
        # However, the problem is that for even positions, the boxes are empty, so we don't need to multiply by M for those
        # Wait, the problem says: boxes at odd positions are already filled, so we don't need to consider them
        # Boxes at even positions are empty, so we need to fill them
        # So the total number of arrangements is M^(number of even positions up to N)
        # The number of even positions up to N is floor(N/2)
        # So the answer is M^(floor(N/2)) mod MOD
        k = N // 2
        ans = pow(M, k, MOD)
        print(ans)

if __name__ == '__main__':
    solve()