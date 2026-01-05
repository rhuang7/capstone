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
    for num in a:
        if freq[num] > 0 and num % 3 != 0:
            result.append(num)
            freq[num] -= 1
            break

    # Now build the sequence by multiplying by 2 or dividing by 3
    while len(result) < n:
        last = result[-1]
        if freq[last * 2] > 0:
            result.append(last * 2)
            freq[last * 2] -= 1
        elif freq[last // 3] > 0:
            result.append(last // 3)
            freq[last // 3] -= 1

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()