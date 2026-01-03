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
    # Start with the number that is not divisible by 3
    # Because the first number cannot be divided by 3
    for num in a:
        if count[num] > 0 and num % 3 != 0:
            result.append(num)
            count[num] -= 1
            break

    # Now build the sequence from the starting number
    # We use a queue to process the numbers
    from collections import deque
    queue = deque()
    queue.append(result[-1])

    while queue:
        current = queue.popleft()
        result.append(current)
        count[current] -= 1

        # Check if current can be multiplied by 2
        if count[current * 2] > 0:
            queue.append(current * 2)
        # Check if current can be divided by 3
        if current % 3 == 0 and count[current // 3] > 0:
            queue.append(current // 3)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()