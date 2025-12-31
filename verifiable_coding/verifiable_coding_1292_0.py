import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(input[ptr]); ptr += 1
    M = int(input[ptr]); ptr += 1
    w = int(input[ptr]); ptr += 1
    b = int(input[ptr]); ptr += 1

    W = set()
    B = set()
    for _ in range(w):
        x = int(input[ptr]); ptr += 1
        y = int(input[ptr]); ptr += 1
        W.add((x, y))
    for _ in range(b):
        x = int(input[ptr]); ptr += 1
        y = int(input[ptr]); ptr += 1
        B.add((x, y))

    total = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (i, j) in W or (i, j) in B:
                continue
            # Ray starts from (i, j)
            # Move right until stop
            count_w = 0
            stop = False
            for k in range(j, M + 1):
                if (i, k) in B:
                    total += (k - j + 1)
                    stop = True
                    break
                if (i, k) in W:
                    count_w += 1
                    if count_w == 2:
                        total += (k - j + 1)
                        stop = True
                        break
            if not stop:
                total += (M - j + 1)

    print(total)

if __name__ == '__main__':
    solve()