import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        is_rainbow = True
        # Check if the array has the correct structure
        # First part: 1 to 7
        # Second part: 6 to 1
        # Check for the first part
        current = 1
        for i in range(N):
            if A[i] != current:
                is_rainbow = False
                break
            if current == 7:
                current = 6
            else:
                current += 1
        if not is_rainbow:
            results.append("no")
            continue
        # Check for the second part
        current = 6
        for i in range(N - 1, -1, -1):
            if A[i] != current:
                is_rainbow = False
                break
            if current == 1:
                current = 2
            else:
                current -= 1
        results.append("yes" if is_rainbow else "no")
    print("\n".join(results))

if __name__ == '__main__':
    solve()