import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        l = list(map(int, data[idx:idx+n]))
        idx += n
        
        locked = []
        unlocked = []
        for i in range(n):
            if l[i] == 1:
                locked.append(a[i])
            else:
                unlocked.append(a[i])
        
        # We need to arrange the unlocked elements such that the prefix sums have as few negative values as possible
        # To minimize k, we want to make the prefix sums as large as possible early on
        # So we sort the unlocked elements in ascending order and place them in the unlocked positions
        # However, we need to be careful with the prefix sums
        # We can try a greedy approach: sort the unlocked elements in ascending order and place them in the unlocked positions
        
        # Create a list of positions where the elements are unlocked
        unlock_positions = []
        for i in range(n):
            if l[i] == 0:
                unlock_positions.append(i)
        
        # Sort the unlocked elements in ascending order
        unlocked_sorted = sorted(unlocked)
        
        # Create the result array
        res = [0] * n
        for i in range(n):
            if l[i] == 1:
                res[i] = a[i]
            else:
                res[i] = unlocked_sorted.pop(0)
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()