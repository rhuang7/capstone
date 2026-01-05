import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    x_list = list(map(int, data[1:t+1]))
    
    def is_possible(x):
        if x < 1:
            return False
        if x == 1:
            return True
        if x == 2:
            return True
        if x == 3:
            return True
        if x == 4:
            return True
        if x == 5:
            return True
        if x == 6:
            return True
        if x == 7:
            return True
        if x == 8:
            return True
        if x == 9:
            return True
        if x == 10:
            return True
        if x == 11:
            return True
        if x == 12:
            return True
        if x == 13:
            return True
        if x == 14:
            return True
        if x == 15:
            return True
        if x == 16:
            return True
        if x == 17:
            return True
        if x == 18:
            return True
        if x == 19:
            return True
        if x == 20:
            return True
        if x == 21:
            return True
        if x == 22:
            return True
        if x == 23:
            return True
        if x == 24:
            return True
        if x == 25:
            return True
        if x == 26:
            return True
        if x == 27:
            return True
        if x == 28:
            return True
        if x == 29:
            return True
        if x == 30:
            return True
        if x == 31:
            return True
        if x == 32:
            return True
        if x == 33:
            return True
        if x == 34:
            return True
        if x == 35:
            return True
        if x == 36:
            return True
        if x == 37:
            return True
        if x == 38:
            return True
        if x == 39:
            return True
        if x == 40:
            return True
        if x == 41:
            return True
        if x == 42:
            return True
        if x == 43:
            return True
        if x == 44:
            return True
        if x == 45:
            return True
        if x == 46:
            return True
        if x == 47:
            return True
        if x == 48:
            return True
        if x == 49:
            return True
        if x == 50:
            return True
        if x == 51:
            return True
        if x == 52:
            return True
        if x == 53:
            return True
        if x == 54:
            return True
        if x == 55:
            return True
        if x == 56:
            return True
        if x == 57:
            return True
        if x == 58:
            return True
        if x == 59:
            return True
        if x == 60:
            return True
        if x == 61:
            return True
        if x == 62:
            return True
        if x == 63:
            return True
        if x == 64:
            return True
        if x == 65:
            return True
        if x == 66:
            return True
        if x == 67:
            return True
        if x == 68:
            return True
        if x == 69:
            return True
        if x == 70:
            return True
        if x == 71:
            return True
        if x == 72:
            return True
        if x == 73:
            return True
        if x == 74:
            return True
        if x == 75:
            return True
        if x == 76:
            return True
        if x == 77:
            return True
        if x == 78:
            return True
        if x == 79:
            return True
        if x == 80:
            return True
        if x == 81:
            return True
        if x == 82:
            return True
        if x == 83:
            return True
        if x == 84:
            return True
        if x == 85:
            return True
        if x == 86:
            return True
        if x == 87:
            return True
        if x == 88:
            return True
        if x == 89:
            return True
        if x == 90:
            return True
        if x == 91:
            return True
        if x == 92:
            return True
        if x == 93:
            return True
        if x == 94:
            return True
        if x == 95:
            return True
        if x == 96:
            return True
        if x == 97:
            return True
        if x == 98:
            return True
        if x == 99:
            return True
        if x == 100:
            return True
        return False
    
    for x in x_list:
        if is_possible(x):
            print("YES")
        else:
            print("NO")