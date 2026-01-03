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
        
        # Precompute the earliest time to solve each problem
        # For easy problems, time is a
        # For hard problems, time is b
        # We need to solve all problems with t_i <= s
        # So we need to find the maximum s such that all problems with t_i <= s can be solved in s time
        
        # We can binary search on s
        # For each s, we check if all problems with t_i <= s can be solved in s time
        # To do that, we can collect all problems with t_i <= s, and check if the total time needed is <= s
        
        # First, collect all problems with t_i <= T (since s can't exceed T)
        # Then, for each s, we can check if all problems with t_i <= s can be solved in s time
        
        # We can precompute the earliest time to solve each problem
        # For each problem, the earliest time to solve it is max(t_i, 0)
        # The total time needed to solve all problems with t_i <= s is the sum of a or b for each such problem
        
        # We can sort the problems by t_i
        # Then, for each s, we can find all problems with t_i <= s, and check if the total time needed is <= s
        
        # We can binary search on s in [0, T]
        # For each candidate s, we can find the number of problems with t_i <= s, and check if the total time needed is <= s
        
        # Precompute the list of (t_i, type)
        # Sort by t_i
        problems = sorted(zip(t, types), key=lambda x: x[0])
        
        # Precompute prefix sums of a and b
        # We will need to know how many easy and hard problems are there up to each t_i
        # So we can create two arrays: easy_count and hard_count
        # easy_count[i] is the number of easy problems in the first i problems
        # hard_count[i] is the number of hard problems in the first i problems
        
        # Also, we can precompute the prefix sum of a and b
        # So that we can compute the total time needed for the first i problems
        
        # We will sort the problems by t_i
        # Then, for each i, we can compute the total time needed to solve the first i problems
        
        # Let's sort the problems by t_i
        problems.sort()
        
        # Now, we can precompute the prefix sums
        # We will have two arrays: easy_count and hard_count
        # And a total_time array
        easy_count = []
        hard_count = []
        total_time = []
        current_easy = 0
        current_hard = 0
        current_time = 0
        for t_i, type_i in problems:
            if type_i == 0:
                current_easy += 1
                current_time += a
            else:
                current_hard += 1
                current_time += b
            easy_count.append(current_easy)
            hard_count.append(current_hard)
            total_time.append(current_time)
        
        # Now, we can binary search on s in [0, T]
        # For each s, we can find the maximum i such that t_i <= s
        # Then, check if the total time needed for the first i problems is <= s
        # If yes, then we can consider this s as a candidate
        
        # We can binary search on s in [0, T]
        # For each s, find the maximum i where t_i <= s
        # Then, check if the total time for the first i problems is <= s
        
        # We can use binary search for this
        # Also, we need to consider that some problems may have t_i > s, but they are not mandatory
        
        # Let's binary search for the best s
        # The maximum possible points is the maximum number of problems that can be solved in s time, where s is such that all mandatory problems up to s are solved
        
        # We can try all possible s in [0, T], but that would be too slow
        # So we need to find the best s efficiently
        
        # We can binary search on s in [0, T]
        # For each s, we find the maximum i such that t_i <= s
        # Then, check if the total time for the first i problems is <= s
        # If yes, then we can consider this s as a candidate
        
        # Also, we need to consider that some problems may have t_i > s, but they are not mandatory
        # So we need to find the maximum s such that all mandatory problems up to s can be solved in s time
        
        # We can binary search on s in [0, T]
        # For each s, we can find the number of problems with t_i <= s
        # Then, check if the total time needed to solve all of them is <= s
        
        # Let's binary search for the best s
        # We'll keep track of the maximum points we can get
        
        max_points = 0
        low = 0
        high = T
        best_s = 0
        
        while low <= high:
            mid = (low + high) // 2
            # Find the number of problems with t_i <= mid
            # We can use binary search for this
            left = 0
            right = n - 1
            best_i = -1
            while left <= right:
                m = (left + right) // 2
                if problems[m][0] <= mid:
                    best_i = m
                    left = m + 1
                else:
                    right = m - 1
            if best_i == -1:
                # No problems with t_i <= mid
                # So we can't solve any problem
                # So the points is 0
                current_points = 0
            else:
                # Check if the total time for the first best_i + 1 problems is <= mid
                total = easy_count[best_i] * a + hard_count[best_i] * b
                if total <= mid:
                    current_points = best_i + 1
                else:
                    current_points = 0
            if current_points > max_points:
                max_points = current_points
                best_s = mid
            if current_points == 0:
                # We can't solve any problem, so we need to try smaller s
                high = mid - 1
            else:
                # Try to find a better s
                low = mid + 1
        
        results.append(max_points)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()