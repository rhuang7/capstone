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
        count = 0
        for i in range(7):
            if i == 0:
                target = 1
            elif i == 6:
                target = 7
            else:
                target = i + 1
            # Find the start and end of the current value
            start = count
            while count < N and A[count] != target:
                count += 1
            if count == N:
                is_rainbow = False
                break
            # Find the end of the current value
            end = count
            while end < N and A[end] == target:
                end += 1
            count = end
            # Check if the count is at least 1
            if end - start == 0:
                is_rainbow = False
                break
        # Check if the array has the correct structure
        # Second part: 6 to 1
        count = 0
        for i in range(6, 0, -1):
            target = i
            # Find the start of the current value
            start = count
            while count < N and A[count] != target:
                count += 1
            if count == N:
                is_rainbow = False
                break
            # Find the end of the current value
            end = count
            while end < N and A[end] == target:
                end += 1
            count = end
            # Check if the count is at least 1
            if end - start == 0:
                is_rainbow = False
                break
        # Check if the array is exactly of length N
        if count != N:
            is_rainbow = False
        results.append("yes" if is_rainbow else "no")
    print("\n".join(results))