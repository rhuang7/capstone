import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        index += 2
        turn = 0
        limak_total = 0
        bob_total = 0
        while True:
            if turn % 2 == 0:
                # Limak's turn
                step = turn // 2 + 1
                if limak_total + step > A:
                    print("Bob")
                    break
                limak_total += step
            else:
                # Bob's turn
                step = (turn // 2) + 1
                if bob_total + step > B:
                    print("Limak")
                    break
                bob_total += step
            turn += 1
        else:
            # This is unreachable as the loop breaks on a win
            pass

if __name__ == '__main__':
    solve()