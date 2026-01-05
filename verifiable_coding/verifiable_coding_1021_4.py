import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    from collections import defaultdict

    # Count frequency of each number
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1

    # Build the sequence
    result = []
    # Start with the number that is not divisible by 3 (since it can't be divided by 3)
    # We need to find the number that is not divisible by 3, which will be the first element
    # We can check all numbers to find the one not divisible by 3
    start = None
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
        if current * 2 in freq and freq[current * 2] > 0:
            freq[current * 2] -= 1
            q.append(current * 2)
        # Check if current can be divided by 3
        if current % 3 == 0 and current // 3 in freq and freq[current // 3] > 0:
            freq[current // 3] -= 1
            q.append(current // 3)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()