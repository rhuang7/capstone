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
        people = [0] * N
        people[0] = 1
        day = 0
        while sum(people) < N:
            day += 1
            can_tell = 0
            for i in range(N):
                if people[i] > 0:
                    can_tell += A[i]
            for i in range(N):
                if people[i] > 0 and can_tell > 0:
                    people[i] = 1
                    can_tell -= 1
        results.append(day)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()