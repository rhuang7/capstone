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
        
        for s in range(0, T + 1):
            # Check if all mandatory problems up to s are solved
            # Count easy and hard problems that have t_i <= s
            # And check if they can be solved in s time
            # We can use binary search to find how many easy and hard problems can be solved
            # For easy problems: total time is a * count
            # For hard problems: total time is b * count
            # Total time must be <= s
            
            # Count easy problems with t_i <= s
            e = len([x for x in easy if x <= s])
            # Count hard problems with t_i <= s
            h = len([x for x in hard if x <= s])
            
            # Check if e easy and h hard can be solved in s time
            # Total time for e easy: e * a
            # Total time for h hard: h * b
            # Total time must be <= s
            if e * a + h * b <= s:
                max_points = max(max_points, e + h)
        
        results.append(max_points)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()