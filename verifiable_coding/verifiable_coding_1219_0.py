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
        
        # Boxes at odd positions are filled, even are empty
        # Total number of partitions to fill is sum of odd positions up to N
        total_partitions = 0
        for i in range(1, N+1, 2):
            total_partitions += i
        
        # The number of ways to arrange M types of jewels in total_partitions partitions
        # is M^total_partitions mod 10^9+7
        result = pow(M, total_partitions, MOD)
        print(result)

if __name__ == '__main__':
    solve()