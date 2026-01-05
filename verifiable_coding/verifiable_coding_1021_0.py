import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    from collections import defaultdict

    # Count frequency of each number
    count = defaultdict(int)
    for num in a:
        count[num] += 1

    # Build the sequence
    result = []
    # Start from the number with the highest value (it's the starting point)
    # We can use a sorted list to find the starting point
    sorted_a = sorted(a)
    start = sorted_a[0]

    # Use a queue to perform BFS to build the sequence
    from collections import deque
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)

    while queue:
        current = queue.popleft()
        result.append(current)
        if count[current] == 0:
            continue
        count[current] -= 1
        # Check if current * 2 is in the list
        if current * 2 in count and count[current * 2] > 0:
            if current * 2 not in visited:
                visited.add(current * 2)
                queue.append(current * 2)
        # Check if current / 3 is in the list
        if current % 3 == 0:
            next_val = current // 3
            if next_val in count and count[next_val] > 0:
                if next_val not in visited:
                    visited.add(next_val)
                    queue.append(next_val)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()