import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        # Compute maximum strength
        # We need to select a subsequence such that the alternating sum is maximized
        # The optimal strategy is to take the largest element, then the smallest, then the next largest, etc.
        # So we sort the array and take elements in a way that maximizes the alternating sum
        # We can do this by sorting the array and then taking the largest, then the smallest, then the next largest, etc.
        # To do this, we can sort the array and then alternate between taking from the end and the beginning
        # We can use a greedy approach: take the largest element, then the smallest, then the next largest, etc.
        # So we sort the array, and then alternate between taking from the end and the beginning
        # Let's sort the array
        a_sorted = sorted(a)
        # Now we alternate between taking from the end and the beginning
        # We'll use two pointers: left and right
        left = 0
        right = n - 1
        res = 0
        turn = 0  # 0 for add, 1 for subtract
        while left <= right:
            if turn == 0:
                res += a_sorted[right]
                right -= 1
            else:
                res -= a_sorted[left]
                left += 1
            turn = 1 - turn
        results.append(str(res))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()