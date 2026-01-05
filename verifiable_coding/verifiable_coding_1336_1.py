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
        count = [0] * 10
        for p in range(a, b + 1):
            for ch in str(p):
                count[int(ch)] += 1
        results.append(f"Case {case_num}: " + " ".join(f"{i}:{count[i]}" for i in range(10)))
        case_num += 1
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()