import sys

MOD = 1000000007

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if N == 0:
            results.append(0)
            continue
        
        # For Nth position, it is visited twice in each round except the first round
        # The first time it is visited in the Kth round
        # The second time it is visited in the (K+1)th round
        # The third time it is visited in the (K+2)th round
        # So we need to find which round the Kth visit occurs
        
        # For the Kth visit to N, it depends on whether K is odd or even
        # If K is odd, it's the first visit in the (K+1)//2 th round
        # If K is even, it's the second visit in the K//2 th round
        
        if K % 2 == 1:
            round_num = (K + 1) // 2
            # Time to reach N in the round_num th round
            time = 2 * (round_num - 1) * N + N
            results.append(time % MOD)
        else:
            round_num = K // 2
            # Time to reach N in the round_num th round
            time = 2 * (round_num - 1) * N + N
            results.append(time % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()