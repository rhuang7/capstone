import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    target_prefix = "LTIME"
    target_suffix = "EMITL"
    required_chars = {}
    for c in target_prefix + target_suffix:
        required_chars[c] = required_chars.get(c, 0) + 1
    
    for s in cases:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        valid = True
        for c, req in required_chars.items():
            if count.get(c, 0) < req:
                valid = False
                break
        if valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()