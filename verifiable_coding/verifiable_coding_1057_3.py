import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    def next_magical(n):
        n = int(n)
        if n == 4:
            return 7
        if n == 7:
            return 47
        if n == 47:
            return 74
        if n == 74:
            return 474
        if n == 474:
            return 744
        if n == 744:
            return 4447
        if n == 4447:
            return 4474
        if n == 4474:
            return 4744
        if n == 4744:
            return 7444
        if n == 7444:
            return 44447
        if n == 44447:
            return 44474
        if n == 44474:
            return 44744
        if n == 44744:
            return 47444
        if n == 47444:
            return 74444
        if n == 74444:
            return 444444
        if n == 444444:
            return 444474
        if n == 444474:
            return 444744
        if n == 444744:
            return 447444
        if n == 447444:
            return 474444
        if n == 474444:
            return 744444
        if n == 744444:
            return 4444444
        if n == 4444444:
            return 4444474
        if n == 4444474:
            return 4444744
        if n == 4444744:
            return 4447444
        if n == 4447444:
            return 4474444
        if n == 4474444:
            return 4744444
        if n == 4744444:
            return 7444444
        if n == 7444444:
            return 44444444
        if n == 44444444:
            return 44444474
        if n == 44444474:
            return 44444744
        if n == 44444744:
            return 44447444
        if n == 44447444:
            return 44474444
        if n == 44474444:
            return 44744444
        if n == 44744444:
            return 47444444
        if n == 47444444:
            return 74444444
        if n == 74444444:
            return 444444444
        if n == 444444444:
            return 444444474
        if n == 444444474:
            return 444444744
        if n == 444444744:
            return 444447444
        if n == 444447444:
            return 444474444
        if n == 444474444:
            return 444744444
        if n == 444744444:
            return 447444444
        if n == 447444444:
            return 474444444
        if n == 474444444:
            return 744444444
        if n == 744444444:
            return 4444444444
        if n == 4444444444:
            return 4444444474
        if n == 4444444474:
            return 4444444744
        if n == 4444444744:
            return 4444447444
        if n == 4444447444:
            return 4444474444
        if n == 4444474444:
            return 4444744444
        if n == 4444744444:
            return 4447444444
        if n == 4447444444:
            return 4474444444
        if n == 4474444444:
            return 4744444444
        if n == 4744444444:
            return 7444444444
        if n == 7444444444:
            return 44444444444
        if n == 44444444444:
            return 44444444474
        if n == 44444444474:
            return 44444444744
        if n == 44444444744:
            return 44444447444
        if n == 44444447444:
            return 44444474444
        if n == 44444474444:
            return 44444744444
        if n == 44444744444:
            return 44447444444
        if n == 44447444444:
            return 44474444444
        if n == 44474444444:
            return 44744444444
        if n == 44744444444:
            return 47444444444
        if n == 47444444444:
            return 74444444444
        if n == 74444444444:
            return 444444444444
        if n == 444444444444:
            return 444444444474
        if n == 444444444474:
            return 444444444744
        if n == 444444444744:
            return 444444447444
        if n == 444444447444:
            return 444444474444
        if n == 444444474444:
            return 444444744444
        if n == 444444744444:
            return 444447444444
        if n == 444447444444:
            return 444474444444
        if n == 444474444444:
            return 44474444444