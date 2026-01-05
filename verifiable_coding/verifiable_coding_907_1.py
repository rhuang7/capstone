import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    R = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(R):
        L = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        valid = True
        i = 0
        while i < L:
            if s[i] == 'H':
                h_pos = i
                i += 1
                while i < L and s[i] == '.':
                    i += 1
                if i >= L or s[i] != 'T':
                    valid = False
                    break
                i += 1
            elif s[i] == 'T':
                valid = False
                break
            else:
                i += 1
        
        if valid and i == L:
            results.append("Valid")
        else:
            results.append("Invalid")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()