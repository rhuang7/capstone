import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            results.append(0)
            continue
        # Find the minimum moves to reach sum >= n
        # The optimal strategy is to increase elements as much as possible before appending
        # Let's find the minimal k such that (k*(k+1))/2 + (k+1) >= n
        # This is equivalent to finding k such that (k^2 + 3k)/2 >= n
        # We can solve this using binary search
        low = 1
        high = 2 * 10**5  # A safe upper bound
        best = 0
        while low <= high:
            mid = (low + high) // 2
            total = (mid * (mid + 1)) // 2 + mid
            if total >= n:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        # The number of moves is best + (n - (best*(best+1)//2)) if needed
        # But since we already found the minimal k, the answer is best + (n - (best*(best+1)//2)) if needed
        # Wait, the actual number of moves is best + (n - (best*(best+1)//2)) if needed
        # But since we have already found the minimal k such that the sum is >= n, the answer is best
        results.append(best)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()