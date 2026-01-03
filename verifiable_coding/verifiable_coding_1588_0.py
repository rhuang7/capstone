import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        while idx < len(data) and data[idx] == b'':
            idx += 1
        if idx >= len(data):
            break
        N = int(data[idx])
        idx += 1
        name_to_ai = {}
        ais = []
        for _ in range(N):
            while idx < len(data) and data[idx] == b'':
                idx += 1
            if idx >= len(data):
                break
            line = data[idx].split()
            idx += 1
            name = line[0].decode()
            ai = int(line[1].decode())
            name_to_ai[name] = ai
            ais.append(ai)
        count = {}
        for ai in ais:
            count[ai] = count.get(ai, 0) + 1
        min_unique = None
        for name, ai in name_to_ai.items():
            if count[ai] == 1:
                if min_unique is None or ai < min_unique:
                    min_unique = ai
        if min_unique is not None:
            for name, ai in name_to_ai.items():
                if ai == min_unique:
                    results.append(name)
                    break
        else:
            results.append("Nobody wins.")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()