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
        
        # Check if the first element of a is 1 or -1
        if a[0] == 1:
            # We can add 1 to any element (including itself) any number of times
            # So any b[i] that is not 0 can be achieved by adding 1 to a[i]
            # But if b[i] is 0, we can't do anything to a[i] (since we can't subtract)
            # So for all elements, if b[i] is not 0, it must be achievable by adding 1 to a[i]
            # But since a[i] is 1, we can add 1 any number of times
            # So for all elements, if b[i] is not 0, it must be possible to reach it by adding 1
            # But since we can add 1 any number of times, it's possible
            # So for a[0] == 1, we can reach any b[i] that is 0 or positive
            # But if b[i] is negative, it's impossible
            for i in range(n):
                if b[i] < 0:
                    possible = False
                    break
            if not possible:
                results.append("NO")
                continue
        elif a[0] == -1:
            # We can add -1 to any element (including itself) any number of times
            # So any b[i] that is not 0 can be achieved by adding -1 to a[i]
            # But if b[i] is 0, we can't do anything to a[i] (since we can't subtract)
            # So for all elements, if b[i] is not 0, it must be achievable by adding -1
            # But since a[i] is -1, we can add -1 any number of times
            # So for all elements, if b[i] is not 0, it must be possible to reach it by adding -1
            # But since we can add -1 any number of times, it's possible
            # So for a[0] == -1, we can reach any b[i] that is 0 or negative
            # But if b[i] is positive, it's impossible
            for i in range(n):
                if b[i] > 0:
                    possible = False
                    break
            if not possible:
                results.append("NO")
                continue
        else:
            # a[0] is 0
            # We can only add 0 to any element (including itself) any number of times
            # So the value of any element can only be 0
            # So all elements in b must be 0
            for i in range(n):
                if b[i] != 0:
                    possible = False
                    break
            if not possible:
                results.append("NO")
                continue
        
        results.append("YES")
    
    print("\n".join(results))