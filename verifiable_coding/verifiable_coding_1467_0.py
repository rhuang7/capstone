import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        k = int(data[idx])
        idx += 1
        hints = []
        for _ in range(k):
            parts = data[idx].split()
            idx += 1
            operator = parts[0]
            li = int(parts[1])
            logical_value = parts[2].decode()
            hints.append((operator, li, logical_value))
        low = 1
        high = 10**9
        min_lies = 0
        for operator, li, logical_value in hints:
            if logical_value == 'Yes':
                if operator == '<':
                    if li >= low:
                        low = li + 1
                elif operator == '>':
                    if li <= high:
                        high = li - 1
                else:  # '='
                    if li != low:
                        min_lies += 1
            else:
                if operator == '<':
                    if li < low:
                        low = li + 1
                elif operator == '>':
                    if li > high:
                        high = li - 1
                else:  # '='
                    if li == low:
                        min_lies += 1
        results.append(str(min_lies))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()