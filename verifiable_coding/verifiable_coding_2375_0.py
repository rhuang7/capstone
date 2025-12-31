import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        count = [0] * 201
        for num in a:
            count[num] += 1
        max_len = 0
        for i in range(201):
            for j in range(i, 201):
                if i == j:
                    max_len = max(max_len, count[i])
                else:
                    left = count[i]
                    right = count[j]
                    mid = 0
                    for k in range(n):
                        if a[k] == i or a[k] == j:
                            if a[k] == i:
                                left -= 1
                            elif a[k] == j:
                                right -= 1
                            else:
                                mid += 1
                    total = left + right + mid
                    if total > max_len:
                        max_len = total
        results.append(str(max_len))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()