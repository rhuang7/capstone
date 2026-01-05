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
        while idx < len(data) and data[idx].strip() == b'':
            idx += 1
        if idx >= len(data):
            break
        N = int(data[idx])
        idx += 1
        name_to_num = {}
        nums = []
        for _ in range(N):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            line = data[idx].split()
            idx += 1
            name = line[0].decode()
            num = int(line[1].decode())
            name_to_num[name] = num
            nums.append(num)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        min_unique = None
        for name, num in name_to_num.items():
            if count[num] == 1:
                if min_unique is None or num < min_unique:
                    min_unique = num
        if min_unique is not None:
            for name, num in name_to_num.items():
                if num == min_unique:
                    results.append(name)
                    break
        else:
            results.append("Nobody wins.")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()