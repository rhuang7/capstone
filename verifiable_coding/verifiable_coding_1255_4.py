import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    for _ in range(T):
        s = data[idx]
        k = int(data[idx+1])
        idx += 2
        
        unique_chars = set(s)
        len_s = len(s)
        
        if k >= len_s:
            print('a' * len_s)
            continue
        
        used = set()
        result = []
        count = 0
        
        # Try to use as many characters as possible that are not in s
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in unique_chars and c not in used:
                result.append(c)
                used.add(c)
                count += 1
                if count == len_s - k:
                    break
        
        # Now fill the rest with characters from s, but not already used
        for c in sorted(unique_chars):
            if c not in used:
                result.append(c)
                used.add(c)
                count += 1
                if count == len_s - k:
                    break
        
        if len(result) < len_s:
            print("NOPE")
        else:
            print(''.join(result))
            
if __name__ == '__main__':
    solve()