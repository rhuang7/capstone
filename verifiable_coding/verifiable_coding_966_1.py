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
        can_jump = [True] * N
        for i in range(N-1):
            if H[i+1] > H[i]:
                if H[i+1] - H[i] > U:
                    can_jump[i+1] = False
            elif H[i+1] < H[i]:
                if H[i+1] - H[i] < -D:
                    can_jump[i+1] = False
        max_reach = 0
        parachute_used = False
        for i in range(N):
            if can_jump[i]:
                max_reach = i + 1
            else:
                if not parachute_used and H[i] > H[i-1]:
                    if H[i] - H[i-1] > U:
                        parachute_used = True
                        max_reach = i
                    else:
                        max_reach = i - 1
                else:
                    max_reach = i - 1
        results.append(str(max_reach))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()