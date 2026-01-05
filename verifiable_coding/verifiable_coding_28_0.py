import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        # Try to find a way to have exactly one occurrence of "abacaba"
        found = False
        result_str = list(s)
        
        # Try each possible starting position for "abacaba"
        for i in range(n - 6):
            # Check if we can replace question marks to form "abacaba" starting at i
            valid = True
            for j in range(7):
                if s[i + j] != '?' and s[i + j] != 'abacaba'[j]:
                    valid = False
                    break
            if valid:
                # Try to replace question marks to form "abacaba" at i
                temp = list(s)
                for j in range(7):
                    if temp[i + j] == '?':
                        temp[i + j] = 'abacaba'[j]
                # Now check how many occurrences of "abacaba" are there in temp
                count = 0
                for k in range(n - 6):
                    if ''.join(temp[k:k+7]) == 'abacaba':
                        count += 1
                if count == 1:
                    found = True
                    result_str = temp
                    break
        
        if found:
            results.append("Yes")
            results.append(''.join(result_str))
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()