import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    from collections import defaultdict

    # Count the frequency of each number
    count = defaultdict(int)
    for num in a:
        count[num] += 1

    # Build the sequence
    result = []
    # Start with the number that is not divisible by 3 (since it can't be divided by 3)
    # So we find the number that is not divisible by 3 and is the starting point
    for num in a:
        if num % 3 != 0:
            start = num
            break

    # Use a queue to build the sequence
    from collections import deque
    q = deque()
    q.append(start)
    while q:
        current = q.popleft()
        result.append(current)
        # Check if current can be multiplied by 2
        if count[current * 2] > 0:
            count[current * 2] -= 1
            q.append(current * 2)
        # Check if current can be divided by 3
        if current % 3 == 0 and count[current // 3] > 0:
            count[current // 3] -= 1
            q.append(current // 3)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()