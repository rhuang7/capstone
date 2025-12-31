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
        # But for Kth time, it depends on how many times it has been visited before
        # For N, the first time it is visited is in round N (going up)
        # The second time is in round N (going down)
        # The third time is in round N+1 (going up)
        # The fourth time is in round N+1 (going down)
        # And so on
        
        # For Kth visit to N:
        # If K is odd, it's during the up journey in some round
        # If K is even, it's during the down journey in some round
        
        # Determine the round and direction
        if K % 2 == 1:
            # Odd K: up journey
            round_num = (K + 1) // 2
            # The up journey to N happens in round_num
            # Time to reach N in up journey: 2 * (round_num - 1) + N
            time = 2 * (round_num - 1) + N
        else:
            # Even K: down journey
            round_num = K // 2
            # The down journey to N happens in round_num
            # Time to reach N in down journey: 2 * (round_num - 1) + 2 * N - 1
            time = 2 * (round_num - 1) + 2 * N - 1
        
        results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()