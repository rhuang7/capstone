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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        D_count = 0
        C_count = 0
        B_count = 0
        A_count = 0
        for score in A:
            if score < 60:
                D_count += 1
            elif 60 <= score < 75:
                C_count += 1
            elif 75 <= score < 90:
                B_count += 1
            else:
                A_count += 1
        if D_count != N//4 or C_count != N//4 or B_count != N//4 or A_count != N//4:
            results.append("-1")
            continue
        # Sort the scores
        A.sort()
        # Find thresholds
        x = A[N//4]
        y = A[2*N//4]
        z = A[3*N//4]
        results.append(f"{x} {y} {z}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()