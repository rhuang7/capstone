import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        if N == 0:
            results.append(0)
            continue
        # Find the round where N is visited for the Kth time
        # In round r, N is visited twice (going up and coming down)
        # Except for the first time when r = N, it's visited once
        # So, for Kth time, if K is odd, it's the first time in some round
        # If K is even, it's the second time in some round
        # Find the round r where N is visited for the Kth time
        # For Kth time:
        # If K is odd, it's the first time in round r = N
        # If K is even, it's the second time in round r = N
        # But if K is larger than the number of times N is visited in rounds up to some r, we need to find the correct r
        # Let's find the r such that the number of times N is visited in rounds 1 to r is >= K
        # For each round r, N is visited twice (except when r = N, it's visited once)
        # So total times N is visited in rounds 1 to r is 2*(r - 1) + 1 if r >= N
        # So we need to find the smallest r such that 2*(r - 1) + 1 >= K
        # If K is odd, r = K // 2 + 1
        # If K is even, r = K // 2
        # But we need to ensure that r >= N
        # So, r = max(N, (K + 1) // 2)
        r = max(N, (K + 1) // 2)
        # Now calculate the time
        # Time to reach N in round r:
        # Time to go up to N: N steps
        # Time to come back to 0: 2*N steps
        # But we need to find the time when Kabir is at N for the Kth time
        # If K is odd: it's the first time in round r
        # If K is even: it's the second time in round r
        # So, if K is odd:
        # Time = (r - 1)*2*N + N
        # If K is even:
        # Time = (r - 1)*2*N + 2*N - 1
        if K % 2 == 1:
            time = (r - 1) * 2 * N + N
        else:
            time = (r - 1) * 2 * N + 2 * N - 1
        results.append(time % MOD)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()