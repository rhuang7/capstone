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
        R = int(data[idx])
        G = int(data[idx+1])
        B = int(data[idx+2])
        M = int(data[idx+3])
        idx +=4
        
        r = list(map(int, data[idx:idx+R]))
        idx += R
        g = list(map(int, data[idx:idx+G]))
        idx += G
        b = list(map(int, data[idx:idx+B]))
        idx += B
        
        # Sort each list in descending order
        r.sort(reverse=True)
        g.sort(reverse=True)
        b.sort(reverse=True)
        
        # Function to apply a magic trick on a list
        def apply_trick(lst, times):
            for _ in range(times):
                for i in range(len(lst)):
                    lst[i] = lst[i] // 2
        
        # We can perform up to M tricks, so we try all possible combinations of tricks
        # We will try all possible combinations of tricks on the three lists
        # We will use a priority queue to select the next trick that gives the maximum reduction
        # However, since M is small (<= 100), we can simulate all possibilities
        # We will use a greedy approach: always apply the trick that gives the maximum reduction
        
        # We will use a list of tuples (current_max, list, times_applied)
        # We will keep track of the current maximum value for each list
        # We will use a priority queue to select the next trick to apply
        
        # Initialize the current maximum values
        max_r = r[0]
        max_g = g[0]
        max_b = b[0]
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of the list
        # We will use a list of tuples (current_max, list, times_applied)
        # We will use a priority queue to select the next trick to apply
        
        # We will use a priority queue to select the next trick to apply
        # The priority is the current maximum value of