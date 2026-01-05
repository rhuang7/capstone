import sys

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    T = int(input[0])
    cases = input[1:T+1]
    
    for case in cases:
        parts = case.split()
        if len(parts) == 1:
            # Only first name, format as first letter capitalized
            formatted = parts[0][0].upper() + parts[0][1:]
            print(formatted)
        else:
            # Format all parts except last as M. K. etc.
            # Last part is always the full name
            formatted = []
            for i in range(len(parts) - 1):
                # Take first letter, capitalize, add '.'
                formatted.append(parts[i][0].upper() + '.')
            # Add the last part, capitalize first letter
            formatted.append(parts[-1][0].upper() + parts[-1][1:])
            # Join all parts
            print(''.join(formatted))

if __name__ == '__main__':
    solve()