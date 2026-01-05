import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    A = list(map(int, data[3:3+N]))
    
    # Count the number of elements <= M
    cnt = 0
    for num in A:
        if num <= M:
            cnt += 1
    
    # If no elements are <= M, answer is 0
    if cnt == 0:
        print(0)
        return
    
    # The number of ways to choose two elements to add K
    # is C(cnt, 2) = cnt * (cnt - 1) // 2
    ways = (cnt * (cnt - 1)) // 2
    
    # The answer is the number of ways to perform the operations
    # modulo 10^9 + 7
    print(ways % MOD)

if __name__ == '__main__':
    solve()