import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    D = int(data[0])
    strings = data[1:D+1]

    def is_special(s):
        n = len(s)
        if n % 2 != 0:
            return False
        half = n // 2
        for i in range(half):
            if s[i] != s[i + half]:
                # Try removing s[i]
                temp = s[:i] + s[i+1:]
                if len(temp) % 2 == 0:
                    if temp[:len(temp)//2] == temp[len(temp)//2:]:
                        return True
                # Try removing s[i + half]
                temp = s[:i + half] + s[i + half + 1:]
                if len(temp) % 2 == 0:
                    if temp[:len(temp)//2] == temp[len(temp)//2:]:
                        return True
        return False

    for s in strings:
        if is_special(s):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()