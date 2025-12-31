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
        t_r = int(data[idx])
        idx += 1
        T_r = list(map(int, data[idx:idx+t_r]))
        idx += t_r
        d_r = int(data[idx])
        idx += 1
        D_r = list(map(int, data[idx:idx+d_r]))
        idx += d_r
        t_s = int(data[idx])
        idx += 1
        T_s = list(map(int, data[idx:idx+t_s]))
        idx += t_s
        d_s = int(data[idx])
        idx += 1
        D_s = list(map(int, data[idx:idx+d_s]))
        idx += d_s
        
        # Check if all truth tasks in T_s are in T_r
        all_truth = all(task in T_r for task in T_s)
        # Check if all dare tasks in D_s are in D_r
        all_dare = all(task in D_r for task in D_s)
        if all_truth and all_dare:
            results.append("yes")
        else:
            results.append("no")
    print("\n".join(results))

if __name__ == '__main__':
    solve()