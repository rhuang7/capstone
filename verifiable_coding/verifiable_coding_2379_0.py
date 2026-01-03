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
        s = data[idx]
        idx += 1
        
        # We need to assign each character to a subsequence such that no two adjacent characters are the same
        # We can track the last used pattern for each subsequence
        # For each character, we try to assign it to a subsequence that ends with the opposite character
        # If no such subsequence exists, we create a new one
        
        # We'll use a list to track the last character of each subsequence
        # For example, if we have subsequences ending with '0' and '1', we can assign the next character to the appropriate one
        last = []
        
        for c in s:
            if c == '0':
                # Try to find a subsequence ending with '1'
                found = False
                for i in range(len(last)):
                    if last[i] == '1':
                        last[i] = '0'
                        found = True
                        break
                if not found:
                    last.append('0')
            else:
                # Try to find a subsequence ending with '0'
                found = False
                for i in range(len(last)):
                    if last[i] == '0':
                        last[i] = '1'
                        found = True
                        break
                if not found:
                    last.append('1')
        
        # The number of subsequences is the length of 'last'
        k = len(last)
        # We need to record which subsequence each character belongs to
        # We'll track the subsequence index for each character
        res = []
        # We'll track the last character of each subsequence
        last_char = []
        # We'll track the subsequence index for each character
        subseq = []
        
        for c in s:
            if c == '0':
                # Try to find a subsequence ending with '1'
                found = False
                for i in range(len(last_char)):
                    if last_char[i] == '1':
                        last_char[i] = '0'
                        subseq.append(i + 1)
                        found = True
                        break
                if not found:
                    last_char.append('0')
                    subseq.append(len(last_char))
            else:
                # Try to find a subsequence ending with '0'
                found = False
                for i in range(len(last_char)):
                    if last_char[i] == '0':
                        last_char[i] = '1'
                        subseq.append(i + 1)
                        found = True
                        break
                if not found:
                    last_char.append('1')
                    subseq.append(len(last_char))
        
        results.append(str(k))
        results.append(' '.join(map(str, subseq)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()