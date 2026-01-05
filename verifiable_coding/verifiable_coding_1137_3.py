import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    target = 20 * 100  # Annabelle's age times 100
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        seen = set()
        found = False
        for num in A:
            complement = target - num
            if complement in seen:
                found = True
                break
            seen.add(num)
        print("Accepted" if found else "Rejected")

if __name__ == '__main__':
    solve()