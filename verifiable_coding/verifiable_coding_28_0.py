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
        
        # Check if it's possible to have exactly one occurrence of "abacaba"
        found = False
        possible = False
        result_str = list(s)
        
        # Try placing "abacaba" at each possible position
        for i in range(n - 6):
            # Check if the current position can be modified to "abacaba"
            valid = True
            for j in range(7):
                if s[i + j] != '?' and s[i + j] != "abacaba"[j]:
                    valid = False
                    break
            if valid:
                # Try to replace the characters to "abacaba"
                temp = list(s)
                for j in range(7):
                    temp[i + j] = "abacaba"[j]
                # Check how many times "abacaba" appears in the new string
                count = 0
                for k in range(n - 6):
                    if ''.join(temp[k:k+7]) == "abacaba":
                        count += 1
                if count == 1:
                    possible = True
                    result_str = temp
                    found = True
                    break
        
        if found:
            results.append("Yes")
            results.append("".join(result_str))
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()