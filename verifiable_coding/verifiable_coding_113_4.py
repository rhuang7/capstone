import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        if a == b:
            results.append(0)
            continue
        diff = abs(b - a)
        five = diff // 5
        remainder = diff % 5
        if remainder == 0:
            results.append(five)
        else:
            # Try using one less 5 and use 2 and 1
            results.append(five + 1)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()