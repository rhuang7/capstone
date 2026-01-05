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
        # We want to select a subsequence with maximum alternating sum
        # The optimal strategy is to take the largest element, then the smallest, then the next largest, etc.
        # So we sort the array and alternate taking from the end and beginning
        a_sorted = sorted(a)
        max_strength = 0
        left = 0
        right = n - 1
        turn = 0  # 0 for add, 1 for subtract
        while left <= right:
            if turn == 0:
                max_strength += a_sorted[right]
                right -= 1
            else:
                max_strength -= a_sorted[left]
                left += 1
            turn = 1 - turn
        results.append(str(max_strength))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()