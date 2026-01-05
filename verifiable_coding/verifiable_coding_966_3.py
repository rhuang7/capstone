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
        for i in range(N-1):
            if H[i+1] > H[i]:
                if H[i+1] - H[i] > U:
                    if can_use_parachute:
                        break
                    else:
                        if H[i+1] - H[i] > U:
                            break
                        else:
                            continue
            elif H[i+1] < H[i]:
                if H[i] - H[i+1] > D:
                    if can_use_parachute:
                        can_use_parachute = False
                        continue
                    else:
                        if H[i] - H[i+1] > D:
                            break
                        else:
                            can_use_parachute = True
                            continue
            else:
                continue
            current += 1
        results.append(current + 1)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()