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
        parts = data[idx].split()
        idx += 1
        activities = int(parts[0])
        origin = parts[1].decode()
        laddus = 0
        for _ in range(activities):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            activity = data[idx].strip().decode()
            idx += 1
            if activity.startswith(b'CONTEST_WON'):
                rank = int(activity.split()[1])
                laddus += 300 + max(0, 20 - rank)
            elif activity == b'TOP_CONTRIBUTOR':
                laddus += 300
            elif activity.startswith(b'BUG_FOUND'):
                severity = int(activity.split()[1])
                laddus += severity
            elif activity == b'CONTEST_HOSTED':
                laddus += 50
        min_redeem = 200 if origin == 'INDIAN' else 400
        results.append(str(laddus // min_redeem))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()