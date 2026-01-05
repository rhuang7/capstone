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
        result = list(s)
        possible = True
        
        # Try each possible position for "abacaba"
        for i in range(n - 6):
            # Check if the current position can be "abacaba"
            valid = True
            for j in range(7):
                if result[i + j] != '?' and result[i + j] != 'abacaba'[j]:
                    valid = False
                    break
            if valid:
                # Check if there are other occurrences of "abacaba"
                count = 0
                for k in range(n - 6):
                    if k == i:
                        continue
                    match = True
                    for l in range(7):
                        if result[k + l] != '?' and result[k + l] != 'abacaba'[l]:
                            match = False
                            break
                    if match:
                        count += 1
                if count == 0:
                    found = True
                    break
                else:
                    possible = False
        
        if found:
            print("Yes")
            for j in range(7):
                result[i + j] = 'abacaba'[j]
            print(''.join(result))
        else:
            print("No")

if __name__ == '__main__':
    solve()