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
        value_indices = {}
        for i in range(N):
            if A[i] not in value_indices:
                value_indices[A[i]] = []
            value_indices[A[i]].append(i)
        found = False
        for key in value_indices:
            indices = value_indices[key]
            if len(indices) >= 2:
                for i in range(len(indices)):
                    for j in range(i+1, len(indices)):
                        if indices[i] != indices[j]:
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
        results.append("Truly Happy" if found else "Poor Chef")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()