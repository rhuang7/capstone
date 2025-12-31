import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    M = int(data[0])
    books = list(map(int, data[1:M+1]))
    N = int(data[M+1])
    queries = list(map(int, data[M+2:]))
    
    # Create a dictionary to map book numbers to their current positions
    book_pos = {book: i for i, book in enumerate(books)}
    
    # Create a list to keep track of the current positions of the books
    positions = list(range(M))
    
    result = []
    
    for q in queries:
        # Find the book at the q-th position (0-based)
        book = books[positions[q-1]]
        result.append(book)
        
        # Remove the book from the list
        del positions[q-1]
        
        # Update the positions of the remaining books
        for i in range(q-1, len(positions)):
            positions[i] -= 1
    
    for num in result:
        print(num)

if __name__ == '__main__':
    solve()