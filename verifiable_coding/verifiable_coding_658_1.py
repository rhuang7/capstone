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
        n = int(data[idx])
        idx += 1
        s = list(map(int, data[idx:idx + n]))
        idx += n
        
        max_len = 0
        # Check the original sequence
        current_len = 1
        for i in range(1, n):
            if (i % 2 == 1 and s[i] >= s[i - 1]) or (i % 2 == 0 and s[i] <= s[i - 1]):
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        
        # Try inserting one element
        for i in range(n):
            # Try inserting before s[i]
            for val in [s[i - 1] - 1, s[i - 1], s[i - 1] + 1, s[i], s[i] + 1]:
                if i == 0:
                    new_s = [val] + s
                else:
                    new_s = s[:i] + [val] + s[i:]
                current_len = 1
                for j in range(1, len(new_s)):
                    if (j % 2 == 1 and new_s[j] >= new_s[j - 1]) or (j % 2 == 0 and new_s[j] <= new_s[j - 1]):
                        current_len += 1
                    else:
                        current_len = 1
                    max_len = max(max_len, current_len)
            # Try inserting after s[i]
            for val in [s[i] - 1, s[i], s[i] + 1, s[i + 1], s[i + 1] + 1]:
                if i == n - 1:
                    new_s = s + [val]
                else:
                    new_s = s[:i + 1] + [val] + s[i + 1:]
                current_len = 1
                for j in range(1, len(new_s)):
                    if (j % 2 == 1 and new_s[j] >= new_s[j - 1]) or (j % 2 == 0 and new_s[j] <= new_s[j - 1]):
                        current_len += 1
                    else:
                        current_len = 1
                    max_len = max(max_len, current_len)
        
        results.append(str(max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()