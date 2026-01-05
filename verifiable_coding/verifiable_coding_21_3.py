import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index + n]))
        index += n
        
        # Convert to a set for fast lookups
        s_set = set(s)
        min_k = -1
        
        # Try all possible k from 1 to 1023
        for k in range(1, 1024):
            new_set = set()
            valid = True
            for num in s:
                new_num = num ^ k
                if new_num in s_set:
                    new_set.add(new_num)
                else:
                    valid = False
                    break
            if valid and len(new_set) == n:
                min_k = k
                break
        
        results.append(str(min_k))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()