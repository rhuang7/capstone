import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # Check if it's possible to have exactly one occurrence of "abacaba"
        found = False
        result = ""
        for i in range(n - 6):
            # Check if we can form "abacaba" starting at position i
            valid = True
            for j in range(7):
                if s[i + j] != '?' and s[i + j] != "abacaba"[j]:
                    valid = False
                    break
            if valid:
                found = True
                # Try to replace '?'s with "abacaba" and check for overlaps
                temp = list(s)
                for j in range(7):
                    if temp[i + j] == '?':
                        temp[i + j] = "abacaba"[j]
                # Check if there is exactly one occurrence
                count = 0
                for k in range(n - 6):
                    if all(temp[k + j] == "abacaba"[j] for j in range(7)):
                        count += 1
                if count == 1:
                    result = ''.join(temp)
                    break
        
        if found:
            print("Yes")
            print(result)
        else:
            print("No")

if __name__ == '__main__':
    solve()