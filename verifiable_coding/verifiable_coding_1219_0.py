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
        # Total number of partitions to fill = sum of odd positions up to N
        total_partitions = 0
        for i in range(1, N+1, 2):
            total_partitions += i
        
        # The answer is M^total_partitions mod 10^9+7
        print(pow(M, total_partitions, MOD))

if __name__ == '__main__':
    solve()