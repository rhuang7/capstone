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
            # Count easy and hard problems that can be solved by s
            # We need to find the maximum number of problems that can be solved by s
            # and ensure that all mandatory problems up to s are solved
            
            # Find the number of easy problems that can be solved by s
            # Each easy problem takes a minutes, so the number of easy problems is s // a
            # But we need to count only those with t_i <= s
            # Similarly for hard problems
            
            # Binary search for the number of easy problems with t_i <= s
            # and can be solved by s
            # Similarly for hard problems
            
            # We can precompute the sorted lists
            # For each s, find the maximum number of easy and hard problems that can be solved by s
            # and that have t_i <= s
            
            # For easy problems:
            # Find the number of easy problems with t_i <= s
            # and the number of easy problems that can be solved by s
            # The minimum of these two is the number of easy problems that can be solved
            
            # For hard problems:
            # Find the number of hard problems with t_i <= s
            # and the number of hard problems that can be solved by s
            # The minimum of these two is the number of hard problems that can be solved
            
            # The total number of problems that can be solved is the sum of the two
            
            # But we need to ensure that all mandatory problems up to s are solved
            # So we need to find the maximum s such that all mandatory problems up to s are solved
            
            # To find the maximum s, we can binary search on s
            
            # Let's find the maximum s such that all mandatory problems up to s are solved
            
            # First, find the set of all mandatory problems
            # For each s, the mandatory problems are those with t_i <= s
            # We need to check if all of them can be solved by s
            
            # So for each s, we need to check:
            # 1. All mandatory problems (t_i <= s) can be solved by s
            # 2. The number of problems solved is the sum of the number of easy and hard problems that can be solved by s
            
            # To do this efficiently, we can precompute the sorted lists of t_i for easy and hard problems
            
            # For each s, we can find the number of easy and hard problems with t_i <= s
            # and the maximum number of easy and hard problems that can be solved by s
            # The minimum of these two is the number of problems that can be solved
            
            # We can binary search for the maximum s where all mandatory problems up to s can be solved
            
            # To do this, we can find the maximum s such that:
            # the number of easy problems with t_i <= s is <= s // a
            # and the number of hard problems with t_i <= s is <= s // b
            
            # So for each s, we need to check if all mandatory problems up to s can be solved by s
            
            # To find the maximum s, we can binary search between 0 and T
            
            # Let's binary search for s
            low = 0
            high = T
            best = 0
            
            while low <= high:
                mid = (low + high) // 2
                # Check if all mandatory problems up to mid can be solved by mid
                # Find the number of easy and hard problems with t_i <= mid
                # and check if they can be solved by mid
                
                # For easy problems
                # Find the number of easy problems with t_i <= mid
                # This is the number of easy problems in the sorted list that are <= mid
                # Similarly for hard problems
                # We can use binary search for this
                
                # For easy problems
                e = 0
                for ti in easy:
                    if ti <= mid:
                        e += 1
                # For hard problems
                h = 0
                for ti in hard:
                    if ti <= mid:
                        h += 1
                # Check if all mandatory problems up to mid can be solved by mid
                # The number of easy problems that can be solved by mid is mid // a
                # The number of hard problems that can be solved by mid is mid // b
                # We need to have e <= mid // a and h <= mid // b
                if e <= mid // a and h <= mid // b:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            # Now, for the best s, compute the maximum number of problems that can be solved
            # This is the number of easy and hard problems that can be solved by s
            # And all mandatory problems up to s are solved
            # So we can compute this as:
            e = 0
            for ti in easy:
                if ti <= best:
                    e += 1
            h = 0
            for ti in hard:
                if ti <= best:
                    h += 1
            max_points = max(max_points, e + h)
        
        results.append(str(max_points))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()