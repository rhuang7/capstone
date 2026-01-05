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
        limak_eaten = 0
        bob_eaten = 0
        while True:
            if turn % 2 == 0:
                # Limak's turn
                if limak_eaten + (turn // 2 + 1) > A:
                    print("Bob")
                    break
                limak_eaten += (turn // 2 + 1)
            else:
                # Bob's turn
                if bob_eaten + (turn // 2 + 1) > B:
                    print("Limak")
                    break
                bob_eaten += (turn // 2 + 1)
            turn += 1

if __name__ == '__main__':
    solve()