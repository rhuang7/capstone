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
        A.sort()
        d_count = 0
        c_count = 0
        b_count = 0
        a_count = 0
        for score in A:
            if score < 60:
                d_count += 1
            elif 60 <= score < 75:
                c_count += 1
            elif 75 <= score < 90:
                b_count += 1
            else:
                a_count += 1
        if d_count != N//4 or c_count != N//4 or b_count != N//4 or a_count != N//4:
            results.append("-1")
            continue
        # Try to find x, y, z
        # We need exactly N/4 students in each grade
        # So we need to find thresholds such that:
        # d: <x
        # c: >=x and <y
        # b: >=y and <z
        # a: >=z
        # So we need to find x, y, z such that:
        # The first N/4 students are D
        # Next N/4 are C
        # Next N/4 are B
        # Last N/4 are A
        # So x is the minimum of the first N/4 students + 1
        # y is the minimum of the next N/4 students + 1
        # z is the minimum of the last N/4 students + 1
        # But we need to make sure that the thresholds are such that the counts are correct
        # So we can try to find x, y, z as follows:
        # x is the minimum of the first N/4 students + 1
        # y is the minimum of the next N/4 students + 1
        # z is the minimum of the last N/4 students + 1
        # But we need to check if this works
        # So let's try this approach
        x = A[N//4] + 1
        y = A[2*N//4] + 1
        z = A[3*N//4] + 1
        # Now check if this works
        # D: <x
        # C: >=x and <y
        # B: >=y and <z
        # A: >=z
        # So we need to count how many are in each category
        d_count = 0
        c_count = 0
        b_count = 0
        a_count = 0
        for score in A:
            if score < x:
                d_count += 1
            elif x <= score < y:
                c_count += 1
            elif y <= score < z:
                b_count += 1
            else:
                a_count += 1
        if d_count == N//4 and c_count == N//4 and b_count == N//4 and a_count == N//4:
            results.append(f"{x} {y} {z}")
        else:
            results.append("-1")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()