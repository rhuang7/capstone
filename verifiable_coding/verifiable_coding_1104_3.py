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
        # In round K, N is visited twice (once going up, once going down)
        # But for Kth time, it depends on how many times N is visited in previous rounds
        # For N, the first time is in round N (going up)
        # The second time is in round N (going down)
        # The third time is in round N+1 (going up)
        # The fourth time is in round N+1 (going down)
        # So for Kth time, if K is odd, it's in round (N + (K-1)//2)
        # if K is even, it's in round (N + (K//2))
        # But we need to check if K is within the number of times N is visited in rounds up to some round
        # The number of times N is visited in rounds up to round m is 2 * (m - N) + 1 if m >= N
        # So we need to find the smallest m such that 2*(m - N) + 1 >= K
        # Solving for m: m >= N + (K-1)//2
        m = N + (K-1)//2
        # Now calculate the time to reach N for the Kth time in round m
        # If K is odd: going up
        # If K is even: going down
        if K % 2 == 1:
            # Going up
            time = 2 * (m - 1) + N
        else:
            # Going down
            time = 2 * m - N - 1
        results.append(time % MOD)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()