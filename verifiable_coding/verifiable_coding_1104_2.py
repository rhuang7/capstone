import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        if N == 0:
            print(0)
            continue
        # Find the round in which N is visited for the Kth time
        # Each round K has 2*K-1 steps
        # The Kth time N is visited is in the (K)th round if N <= K
        # Otherwise, it's in the (K)th round if N > K
        # For N <= K, the Kth time is at the end of the Kth round
        # For N > K, the Kth time is during the (N)th round
        # So the round is max(K, N)
        round = max(K, N)
        # Time to reach N for the Kth time
        # If N <= K: it's the Kth time in the Kth round
        # Time = (2*K - 1) - (K - N) - 1 = K + N - 1
        # If N > K: it's the Kth time in the Nth round
        # Time = (2*N - 1) - (N - K) - 1 = N + K - 1
        time = (N + K - 1) % MOD
        print(time)

if __name__ == '__main__':
    solve()