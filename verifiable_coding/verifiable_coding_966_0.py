import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, U, D = map(int, data[idx:idx+3])
        idx += 3
        H = list(map(int, data[idx:idx+N]))
        idx += N
        can_use_parachute = False
        current = 0
        for i in range(1, N):
            if H[i] == H[current]:
                current = i
                continue
            if H[i] > H[current]:
                if H[i] - H[current] <= U:
                    current = i
                else:
                    results.append(current + 1)
                    break
            else:
                if H[i] < H[current]:
                    if H[i] < H[current] - D:
                        if not can_use_parachute:
                            can_use_parachute = True
                            current = i
                        else:
                            results.append(current + 1)
                            break
                    else:
                        current = i
                else:
                    results.append(current + 1)
                    break
        if current == N-1:
            results.append(N)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()