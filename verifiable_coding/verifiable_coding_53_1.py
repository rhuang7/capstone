import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        # Minimum LIS sequence
        min_seq = []
        stack = []
        for c in s:
            if c == '<':
                stack.append(1)
            else:
                stack.append(0)
        # Build the sequence
        min_seq = [0] * n
        val = 1
        for i in range(n):
            if stack[i] == 1:
                min_seq[i] = val
                val += 1
            else:
                min_seq[i] = val
                val -= 1
        
        # Maximum LIS sequence
        max_seq = []
        stack = []
        for c in s:
            if c == '<':
                stack.append(1)
            else:
                stack.append(0)
        # Build the sequence
        max_seq = [0] * n
        val = n
        for i in range(n-1, -1, -1):
            if stack[i] == 1:
                max_seq[i] = val
                val -= 1
            else:
                max_seq[i] = val
                val += 1
        
        print(' '.join(map(str, min_seq)))
        print(' '.join(map(str, max_seq)))

if __name__ == '__main__':
    solve()