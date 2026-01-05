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
        possible = False
        result = list(s)
        
        # Try each possible position for "abacaba"
        for i in range(n - 6):
            # Check if the current position can be "abacaba"
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
                    # Replace '?' with 'abacaba' and check if it's valid
                    temp = list(s)
                    for j in range(7):
                        if temp[i + j] == '?':
                            temp[i + j] = 'abacaba'[j]
                    # Check if this string has exactly one occurrence of "abacaba"
                    count = 0
                    for k in range(n - 6):
                        valid2 = True
                        for l in range(7):
                            if temp[k + l] != '?' and temp[k + l] != 'abacaba'[l]:
                                valid2 = False
                                break
                        if valid2:
                            count += 1
                    if count == 1:
                        possible = True
                        result = temp
                        found = True
                        break
        if found:
            print("Yes")
            print(''.join(result))
        else:
            print("No")

if __name__ == '__main__':
    solve()