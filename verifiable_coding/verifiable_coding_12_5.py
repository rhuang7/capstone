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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
        
        possible = True
        for i in range(n):
            if a[i] != b[i]:
                possible = False
                break
        
        if not possible:
            results.append("NO")
            continue
        
        # Check if a can be transformed into b
        # For each element in b, check if it can be achieved by adding a_i to a_j
        # Since a contains only -1, 0, 1, we can analyze the possibilities
        
        # For each element in b, check if it is achievable
        # The key observation is that the sum of all elements in a must be equal to the sum of all elements in b
        # Because each operation adds a_i to a_j, which doesn't change the total sum of the array
        # So the sum of a and b must be equal
        
        sum_a = sum(a)
        sum_b = sum(b)
        if sum_a != sum_b:
            results.append("NO")
            continue
        
        # Now check for each element in b
        # For each element in b, check if it can be achieved by adding a_i to a_j
        # Since a contains only -1, 0, 1, we can use the following logic:
        # For each element in b, the number of 1's and -1's in a must be sufficient to reach it
        
        # Count the number of 1's, 0's, and -1's in a
        count_1 = a.count(1)
        count_0 = a.count(0)
        count_neg1 = a.count(-1)
        
        # For each element in b, check if it can be achieved
        for num in b:
            if num == 1:
                # We need at least one 1 in a
                if count_1 == 0:
                    possible = False
                    break
            elif num == -1:
                # We need at least one -1 in a
                if count_neg1 == 0:
                    possible = False
                    break
            elif num == 0:
                # We need at least one 0 in a
                if count_0 == 0:
                    possible = False
                    break
            else:
                # For numbers other than -1, 0, 1, it's impossible
                possible = False
                break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()