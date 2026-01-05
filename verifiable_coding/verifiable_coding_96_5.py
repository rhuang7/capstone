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
            # Calculate how many easy and hard problems can be solved by s
            # For easy problems, total time is a * count
            # For hard problems, total time is b * count
            # We need to find the maximum number of problems that can be solved by s
            
            # Try all possible combinations of easy and hard problems
            # We can use binary search to find the maximum number of easy and hard problems that can be solved by s
            
            # First, find the maximum number of easy problems that can be solved by s
            # We need to select the earliest easy problems
            # So we can binary search the maximum number of easy problems that can be solved by s
            # Similarly for hard problems
            
            # Find the maximum number of easy problems that can be solved by s
            # We can binary search on the number of easy problems
            low = 0
            high = len(easy)
            max_easy = 0
            while low <= high:
                mid = (low + high) // 2
                if mid * a <= s:
                    max_easy = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            # Find the maximum number of hard problems that can be solved by s
            low = 0
            high = len(hard)
            max_hard = 0
            while low <= high:
                mid = (low + high) // 2
                if mid * b <= s:
                    max_hard = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            # Now, we need to check if all mandatory problems up to s are solved
            # For each problem, if t_i <= s, it must be solved
            # So we need to check if all such problems are included in the max_easy and max_hard
            
            # For easy problems, we need to select the earliest ones
            # So we can find how many easy problems have t_i <= s
            # Similarly for hard problems
            
            # Find the number of easy problems with t_i <= s
            easy_count = 0
            for time in easy:
                if time <= s:
                    easy_count += 1
                else:
                    break
            
            # Find the number of hard problems with t_i <= s
            hard_count = 0
            for time in hard:
                if time <= s:
                    hard_count += 1
                else:
                    break
            
            # Now, check if the max_easy and max_hard can cover the easy_count and hard_count
            if max_easy >= easy_count and max_hard >= hard_count:
                total = easy_count + hard_count
                if total > max_points:
                    max_points = total
        
        results.append(max_points)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()