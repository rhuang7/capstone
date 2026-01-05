import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    case_num = 1
    results = []
    while True:
        a = int(input[idx])
        idx += 1
        b = int(input[idx])
        idx += 1
        if a == 0 and b == 0:
            break
        counts = [0] * 10
        for p in range(a, b + 1):
            for c in str(p):
                counts[int(c)] += 1
        result = "Case {}: ".format(case_num)
        for i in range(10):
            result += "{}:{} ".format(i, counts[i])
        results.append(result)
        case_num += 1
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()