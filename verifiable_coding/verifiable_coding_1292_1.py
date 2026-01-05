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

    # For each row
    for i in range(1, N + 1):
        # For each column
        for j in range(1, M + 1):
            if (i, j) in W or (i, j) in B:
                continue
            # Start ray from (i, j)
            # Track the number of W's encountered
            w_count = 0
            # Track the position where the ray stops
            stop = j
            for k in range(j, M + 1):
                if (i, k) in B:
                    stop = k
                    break
                if (i, k) in W:
                    w_count += 1
                    if w_count == 2:
                        stop = k
                        break
            # Calculate distance
            total += stop - j + 1

    print(total)

if __name__ == '__main__':
    solve()