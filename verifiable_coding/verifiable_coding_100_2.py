import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        r = int(data[index])
        g = int(data[index+1])
        b = int(data[index+2])
        index += 3
        # The maximum number of days is determined by the sum of the two smaller piles
        # or (total - max_pile) if the sum of the two smaller is less than (total - max_pile)
        max_pile = max(r, g, b)
        sum_other = r + g + b - max_pile
        result = min(sum_other, (r + g + b) // 2)
        results.append(result)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()