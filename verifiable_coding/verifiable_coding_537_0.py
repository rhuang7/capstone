import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    a = list(map(int, data[2:2+n]))
    a.sort()
    total = 0
    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] - a[i] >= k:
                right = mid - 1
            else:
                left = mid + 1
        total += (n - left)
    print(total)

if __name__ == '__main__':
    solve()