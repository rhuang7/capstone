import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        parts = case.split()
        if len(parts) == 1:
            # Only first name, format as first letter capital + rest lowercase
            formatted = parts[0][0].upper() + parts[0][1:].lower()
        else:
            # Format all parts except last as M. K. etc., last as full name
            formatted = ''
            for i in range(len(parts) - 1):
                # Take first letter, capitalize, add '.'
                formatted += parts[i][0].upper() + '.'
            # Format last name: first letter capital, rest lowercase
            formatted += parts[-1][0].upper() + parts[-1][1:].lower()
        print(formatted)

if __name__ == '__main__':
    solve()