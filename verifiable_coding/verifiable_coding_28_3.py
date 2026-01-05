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
        # Try placing "abacaba" at each possible position
        found = False
        possible = []
        for i in range(n - 6):
            # Check if the substring can be transformed to "abacaba"
            valid = True
            for j in range(7):
                if s[i + j] != '?' and s[i + j] != 'abacaba'[j]:
                    valid = False
                    break
            if valid:
                # Check if there are other occurrences of "abacaba"
                count = 0
                for k in range(n - 6):
                    if k == i:
                        continue
                    valid2 = True
                    for l in range(7):
                        if s[k + l] != '?' and s[k + l] != 'abacaba'[l]:
                            valid2 = False
                            break
                    if valid2:
                        count += 1
                if count == 0:
                    found = True
                    # Replace '?' with 'abacaba' and record the string
                    temp = list(s)
                    for j in range(7):
                        if temp[i + j] == '?':
                            temp[i + j] = 'abacaba'[j]
                    possible.append(''.join(temp))
                    break
        
        if found:
            results.append("Yes")
            results.append(possible[0])
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()