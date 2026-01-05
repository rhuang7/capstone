import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        t_r = int(data[idx])
        idx += 1
        T_r = list(map(int, data[idx:idx + t_r]))
        idx += t_r
        d_r = int(data[idx])
        idx += 1
        D_r = list(map(int, data[idx:idx + d_r]))
        idx += d_r
        t_s = int(data[idx])
        idx += 1
        T_s = list(map(int, data[idx:idx + t_s]))
        idx += t_s
        d_s = int(data[idx])
        idx += 1
        D_s = list(map(int, data[idx:idx + d_s]))
        idx += d_s
        
        # Check if all truth tasks Shyam asks are in Ram's truth tasks
        all_truth = all(t in T_r for t in T_s)
        # Check if all dare tasks Shyam asks are in Ram's dare tasks
        all_dare = all(d in D_r for d in D_s)
        
        if all_truth and all_dare:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()