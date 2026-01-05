import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    w = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    
    W = set()
    for _ in range(w):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        W.add((x, y))
    
    B = set()
    for _ in range(b):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
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
    
    # For each cell (i, j)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (i, j) in W_set or (i, j) in B_set:
                continue
            # Ray starts from (i, j)
            # Move right
            count_w = 0
            end = j
            for k in range(j, M+1):
                if (i, k) in B_set:
                    end = k
                    break
                if (i, k) in W_set:
                    count_w += 1
                    if count_w == 2:
                        end = k
                        break
            # Calculate distance
            total += end - j + 1
    
    print(total)

if __name__ == '__main__':
    solve()