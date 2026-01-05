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

    # For each cell (i, j)
    for i in range(1, N+1):
        # For each column j
        for j in range(1, M+1):
            if (i, j) in W or (i, j) in B:
                continue
            # Start ray from (i, j)
            # Track the number of W's encountered
            w_count = 0
            # Track the current position
            k = j
            while k <= M:
                if (i, k) in B:
                    # Ray stops at B
                    total += (k - j + 1)
                    break
                if (i, k) in W:
                    w_count += 1
                    if w_count == 2:
                        # Ray stops at second W
                        total += (k - j + 1)
                        break
                k += 1
            else:
                # Ray reached the end of the row
                total += (M - j + 1)

    print(total)

if __name__ == '__main__':
    solve()