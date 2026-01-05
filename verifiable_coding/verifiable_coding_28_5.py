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
        possible = False
        best_str = None
        
        for i in range(n - 6):
            # Check if placing "abacaba" starting at i is possible
            valid = True
            for j in range(7):
                if s[i + j] != '?' and s[i + j] != 'abacaba'[j]:
                    valid = False
                    break
            if valid:
                # Try to replace question marks with 'abacaba' and check for other occurrences
                temp = list(s)
                for j in range(7):
                    if temp[i + j] == '?':
                        temp[i + j] = 'abacaba'[j]
                new_s = ''.join(temp)
                
                # Count occurrences of "abacaba" in new_s
                count = 0
                for k in range(len(new_s) - 6):
                    if new_s[k:k+7] == 'abacaba':
                        count += 1
                if count == 1:
                    possible = True
                    best_str = new_s
                    found = True
                    break
        
        if possible:
            results.append("Yes")
            results.append(best_str)
        else:
            results.append("No")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()