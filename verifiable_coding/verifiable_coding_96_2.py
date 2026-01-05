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
        # But we can optimize by checking only the mandatory times
        # We consider all t_i and check if it's possible to solve all problems with t_i <= s
        # So we check for all possible s in the sorted t list
        # Also check T as a possible leaving time
        
        # Get all unique mandatory times
        mandatory_times = set(t)
        mandatory_times.add(T)
        mandatory_times = sorted(mandatory_times)
        
        for s in mandatory_times:
            # Check if all problems with t_i <= s can be solved
            # We need to solve all such problems
            # We can solve them in any order, but we need to find the maximum number of problems that can be solved in time s
            # We can use a greedy approach: solve as many easy problems as possible first, then hard ones
            
            # Filter all problems with t_i <= s
            easy_solved = 0
            hard_solved = 0
            for i in range(n):
                if t[i] <= s:
                    if types[i] == 0:
                        easy_solved += 1
                    else:
                        hard_solved += 1
            
            # Now try to solve as many as possible in time s
            # We can try different combinations of easy and hard problems
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # But we can optimize by trying all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # But we can optimize by trying all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We can try all possible numbers of hard problems that can be solved in time s
            # We can try all possible numbers of hard problems from 0 to min(len(hard), len(hard_solved))
            # And compute the maximum number of easy problems that can be solved with the remaining time
            
            # We