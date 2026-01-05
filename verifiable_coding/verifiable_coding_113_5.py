import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        if a == b:
            results.append(0)
            continue
        diff = abs(b - a)
        five = diff // 5
        rem = diff % 5
        if rem == 0:
            results.append(five)
        else:
            results.append(five + 1)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()