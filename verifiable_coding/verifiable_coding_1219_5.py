import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        
        # Boxes at odd positions are full, even positions are empty
        # Total number of partitions is sum of odd positions up to N
        # Sum of first k odd numbers is k^2
        k = (N + 1) // 2
        total_partitions = k * k
        
        # Answer is M^total_partitions mod 10^9+7
        result = pow(M, total_partitions, MOD)
        print(result)

if __name__ == '__main__':
    solve()