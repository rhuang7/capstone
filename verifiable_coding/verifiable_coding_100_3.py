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
        # The maximum number of days is the minimum between the sum of the two smaller piles and the total divided by 2
        # Because each day she eats two candies, and she can't eat more than the total number of candies divided by 2
        # Also, the sum of the two smaller piles can't exceed the total
        # So the answer is min((r + g + b) // 2, min(r, g, b) + min(max(r, g, b), sum(r, g, b) - max(r, g, b)))
        # But a simpler way is to take the minimum between the sum of the two smaller piles and the total divided by 2
        # Because if the two smaller piles sum to more than the total divided by 2, then the total divided by 2 is the limiting factor
        # So the answer is min((r + g + b) // 2, r + g + b - max(r, g, b))
        max_val = max(r, g, b)
        sum_other = r + g + b - max_val
        result = min((r + g + b) // 2, sum_other)
        results.append(result)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()