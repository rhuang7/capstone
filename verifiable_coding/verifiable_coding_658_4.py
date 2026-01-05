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
        # Check without inserting any element
        # Find the longest UpDown subsegment
        for i in range(n):
            length = 1
            for j in range(i + 1, n):
                if (j - i) % 2 == 0:
                    if s[j] >= s[j - 1]:
                        length += 1
                    else:
                        break
                else:
                    if s[j] <= s[j - 1]:
                        length += 1
                    else:
                        break
            max_len = max(max_len, length)
        
        # Check with inserting one element
        for i in range(n):
            for val in range(s[i] - 1, s[i] + 1):
                # Insert val between s[i] and s[i+1]
                new_s = s[:i+1] + [val] + s[i+1:]
                length = 1
                for j in range(len(new_s)):
                    if j == 0:
                        continue
                    if (j - 1) % 2 == 0:
                        if new_s[j] >= new_s[j - 1]:
                            length += 1
                        else:
                            break
                    else:
                        if new_s[j] <= new_s[j - 1]:
                            length += 1
                        else:
                            break
                max_len = max(max_len, length)
        
        results.append(str(max_len))
    
    print('\n'.join(results))