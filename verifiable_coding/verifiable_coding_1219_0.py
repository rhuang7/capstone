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
        
        # Boxes at odd positions are full (1, 3, 5, ...)
        # Boxes at even positions are empty (2, 4, 6, ...)
        # We need to count the number of ways to fill the odd boxes with M types of jewels
        # Each odd box has i partitions (i is the position), and each partition can hold one jewel
        # So total number of positions to fill is sum_{i odd <= N} i = (ceil(N/2))^2
        # So the total number of arrangements is M^(total_positions)
        
        total_positions = ((N + 1) // 2) ** 2
        ans = pow(M, total_positions, MOD)
        print(ans)

if __name__ == '__main__':
    solve()