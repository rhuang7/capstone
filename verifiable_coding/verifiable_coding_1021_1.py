import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    from collections import defaultdict

    count = defaultdict(int)
    for num in a:
        count[num] += 1

    result = []
    # Start from the number with the highest value, as it's the starting point
    # We'll build the sequence by multiplying by 2 or dividing by 3
    # We'll use a queue to process numbers in order
    from collections import deque

    # Find the starting number (the one that can't be divided by 3)
    start = None
    for num in a:
        if count[num] == 1:
            start = num
            break

    # Use a queue to process numbers
    queue = deque()
    queue.append(start)
    count[start] -= 1
    if count[start] == 0:
        del count[start]

    while queue:
        current = queue.popleft()
        result.append(current)
        # Check if current can be divided by 3
        if current % 3 == 0:
            next_val = current // 3
            if count[next_val] > 0:
                count[next_val] -= 1
                if count[next_val] == 0:
                    del count[next_val]
                queue.append(next_val)
        # Check if current can be multiplied by 2
        next_val = current * 2
        if count[next_val] > 0:
            count[next_val] -= 1
            if count[next_val] == 0:
                del count[next_val]
            queue.append(next_val)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()