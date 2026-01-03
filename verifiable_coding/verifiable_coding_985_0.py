import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    dp = []
    for num in a:
        idx = bisect.bisect_right(dp, num)
        if idx == 0:
            dp.insert(0, num)
        else:
            dp[idx-1] = num
    print(len(dp))

if __name__ == '__main__':
    solve()