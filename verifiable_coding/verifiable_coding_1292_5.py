import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(input[ptr]); ptr +=1
    M = int(input[ptr]); ptr +=1
    w = int(input[ptr]); ptr +=1
    b = int(input[ptr]); ptr +=1

    W = set()
    B = set()
    for _ in range(w):
        x = int(input[ptr]); ptr +=1
        y = int(input[ptr]); ptr +=1
        W.add((x, y))
    for _ in range(b):
        x = int(input[ptr]); ptr +=1
        y = int(input[ptr]); ptr +=1
        B.add((x, y))

    total = 0

    # Preprocess B cells
    B_set = set()
    for x, y in B:
        B_set.add((x, y))

    # Preprocess W cells
    W_set = set()
    for x, y in W:
        W_set.add((x, y))

    # For each row, process the cells
    for i in range(1, N+1):
        # Track the state of the ray
        state = 0  # 0: normal, 1: passed one W
        prev_w = -1
        for j in range(1, M+1):
            if (i, j) in B_set:
                # Ray stops at B
                total += (j - prev_w) if prev_w != -1 else j
                state = 0
                prev_w = -1
            elif (i, j) in W_set:
                if state == 0:
                    state = 1
                    prev_w = j
                else:
                    # Second W, ray stops
                    total += (j - prev_w)
                    state = 0
                    prev_w = -1
            else:
                # Dot cell, continue
                if state == 0:
                    prev_w = j
                else:
                    total += (j - prev_w)
                    state = 0
                    prev_w = -1
        # After processing the row, handle any remaining state
        if state == 1:
            total += (M - prev_w)
        elif state == 0 and prev_w != -1:
            total += (M - prev_w)

    print(total)

if __name__ == '__main__':
    solve()