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
        remaining = 26 - len(unique_chars)
        
        # Greedily choose the smallest possible characters not in s
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in unique_chars and len(used) < remaining:
                result.append(c)
                used.add(c)
        
        # Now choose the smallest possible characters from s
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in unique_chars and c not in used:
                result.append(c)
                used.add(c)
        
        # Check if we have enough characters
        if len(result) < len_s:
            print("NOPE")
        else:
            print(''.join(result))
    
if __name__ == '__main__':
    solve()