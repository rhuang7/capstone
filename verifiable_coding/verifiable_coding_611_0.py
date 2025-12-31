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
        value_to_index = {}
        for i in range(N):
            if A[i] not in value_to_index:
                value_to_index[A[i]] = []
            value_to_index[A[i]].append(i)
        found = False
        for val in value_to_index:
            indices = value_to_index[val]
            if len(indices) >= 2:
                i = indices[0]
                j = indices[1]
                if A[i] != A[j]:
                    found = True
                    break
        if found:
            results.append("Truly Happy")
        else:
            results.append("Poor Chef")
    print("\n".join(results))

if __name__ == '__main__':
    solve()