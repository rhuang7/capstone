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
        
        # For N >= 1
        # The K-th time Chef reaches N is in the (K)th round if K <= (N+1)
        # Otherwise, it's in the (K + N - 1)th round
        if K <= N:
            # First occurrence in the K-th round
            time = (2 * (K - 1)) * N - (K - 1)
            results.append(time % MOD)
        else:
            # After the first N+1 occurrences
            # The K-th occurrence is in the (K + N - 1)th round
            round_num = K + N - 1
            time = (2 * (round_num - 1)) * N - (round_num - 1)
            results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()