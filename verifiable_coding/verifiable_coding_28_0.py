import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # Try to find a way to have exactly one occurrence of "abacaba"
        found = False
        result = None
        
        # Try each possible starting position for "abacaba"
        for i in range(n - 6):
            # Check if we can replace question marks to make "abacaba" start at i
            valid = True
            for j in range(7):
                if s[i + j] != '?' and s[i + j] != "abacaba"[j]:
                    valid = False
                    break
            if valid:
                # Now check how many occurrences of "abacaba" are there in the string
                # Replace the question marks with "abacaba"
                temp = list(s)
                for j in range(7):
                    temp[i + j] = "abacaba"[j]
                temp_str = ''.join(temp)
                
                # Count occurrences of "abacaba"
                count = 0
                for k in range(n - 6):
                    if temp_str[k:k+7] == "abacaba":
                        count += 1
                if count == 1:
                    found = True
                    result = temp_str
                    break
        
        if found:
            results.append("Yes")
            results.append(result)
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()