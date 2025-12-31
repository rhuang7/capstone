import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        parts = case.split()
        if len(parts) == 1:
            # Only first name
            formatted = parts[0].decode().capitalize()
        else:
            # Multiple parts, format all except last
            formatted = []
            for i in range(len(parts)-1):
                # Take first letter and add '.'
                formatted_part = parts[i].decode()[0].upper() + '.'
                formatted.append(formatted_part)
            # Add last name capitalized
            formatted.append(parts[-1].decode().capitalize())
            formatted = ''.join(formatted)
        print(formatted)

if __name__ == '__main__':
    solve()