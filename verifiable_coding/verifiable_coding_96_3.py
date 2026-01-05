import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    m = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(m):
        n = int(data[idx])
        T = int(data[idx+1])
        a = int(data[idx+2])
        b = int(data[idx+3])
        idx += 4
        types = list(map(int, data[idx:idx+n]))
        idx += n
        t = list(map(int, data[idx:idx+n]))
        idx += n
        
        easy = []
        hard = []
        for i in range(n):
            if types[i] == 0:
                easy.append(t[i])
            else:
                hard.append(t[i])
        
        easy.sort()
        hard.sort()
        
        max_points = 0
        
        # Try all possible leaving times s from 0 to T
        # But we can optimize by checking only the times when problems become mandatory
        # So we collect all unique t_i and check those
        unique_times = set(t)
        for s in unique_times:
            if s > T:
                continue
            # Check if all mandatory problems up to s can be solved
            # Count how many easy and hard problems have t_i <= s
            # And check if they can be solved in s time
            # We can use greedy approach: solve as many easy as possible first
            # Then hard
            remaining_time = s
            easy_count = 0
            hard_count = 0
            for ti in easy:
                if ti > s:
                    break
                if remaining_time >= a:
                    easy_count += 1
                    remaining_time -= a
            for ti in hard:
                if ti > s:
                    break
                if remaining_time >= b:
                    hard_count += 1
                    remaining_time -= b
            total = easy_count + hard_count
            if total > max_points:
                max_points = total
        
        # Also check s = T
        remaining_time = T
        easy_count = 0
        hard_count = 0
        for ti in easy:
            if ti > T:
                break
            if remaining_time >= a:
                easy_count += 1
                remaining_time -= a
        for ti in hard:
            if ti > T:
                break
            if remaining_time >= b:
                hard_count += 1
                remaining_time -= b
        total = easy_count + hard_count
        if total > max_points:
            max_points = total
        
        results.append(str(max_points))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()