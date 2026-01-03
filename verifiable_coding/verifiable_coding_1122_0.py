import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().split()
    n = int(input[0])
    
    total = 0
    ravi_questions = 0
    jhon_questions = 0
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            total += i * i
        else:
            total += 2 * i * i
    
    if total % 2 == 0:
        ravi_questions += 2
    else:
        jhon_questions += 2
    
    if ravi_questions > jhon_questions:
        print("Ravi")
    else:
        print("Jhon")

if __name__ == '__main__':
    solve()