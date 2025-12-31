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
        
        # Sort problems by their mandatory time
        problems = sorted(zip(t, types), key=lambda x: x[0])
        
        # For each possible leaving time s, check if all mandatory problems up to s are solved
        # We'll use binary search to find the maximum s where all mandatory problems up to s can be solved
        # We'll precompute the earliest time to solve all mandatory problems up to s
        
        # Precompute for each problem whether it is mandatory at s
        # We'll use a greedy approach to solve as many as possible
        
        # For each s, we need to solve all problems with t_i <= s
        # We'll find the maximum s where the total time to solve all mandatory problems up to s is <= s
        
        # We'll use binary search on s from 0 to T
        left = 0
        right = T
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            # Check if all mandatory problems up to mid can be solved
            # We'll collect all problems with t_i <= mid
            # Then solve them greedily, trying to solve easy ones first
            # Because easy ones take less time
            
            # Collect all mandatory problems up to mid
            mandatory = []
            for t_i, type_i in problems:
                if t_i <= mid:
                    mandatory.append(type_i)
            
            # Sort mandatory problems by type (easy first)
            mandatory.sort()
            
            # Solve them greedily
            time_used = 0
            count = 0
            for typ in mandatory:
                if typ == 0:
                    time_used += a
                    count += 1
                else:
                    time_used += b
                    count += 1
                if time_used > mid:
                    break
            
            if time_used <= mid:
                best = max(best, count)
                left = mid + 1
            else:
                right = mid - 1
        
        results.append(best)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()