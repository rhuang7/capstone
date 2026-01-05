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
        
        # For Nth position, it is visited twice in each round except the first round
        # The first time it is visited in the Kth round
        # The second time it is visited in the (K+1)th round
        # The third time it is visited in the (K+2)th round
        # And so on
        
        # Find the round where the Kth visit happens
        if K == 1:
            # First visit is during the Nth round
            time = 2 * N - 1
            results.append(time)
        else:
            # For K > 1, the Kth visit is in the (K + N - 1)th round
            round_num = K + N - 1
            # Time to reach N in the round_numth round
            time = 2 * (round_num - 1) * N - (N - 1)
            results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()