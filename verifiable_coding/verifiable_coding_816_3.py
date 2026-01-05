import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    M = int(data[0])
    books = list(map(int, data[1:M+1]))
    N = int(data[M+1])
    queries = list(map(int, data[M+2:M+2+N]))
    
    # Create a dictionary to map book numbers to their current positions
    book_pos = {book: i for i, book in enumerate(books)}
    
    # For each query, find the book at the given position
    # Remove the book from the list and update the positions
    for i in range(N):
        pos = queries[i]
        # Get the book at the current position
        book = books[pos - 1]
        # Remove the book from the list
        books.pop(pos - 1)
        # Update the positions of the remaining books
        for j in range(pos - 1, len(books)):
            book_pos[books[j]] = j
        # Output the book
        print(book)
        
if __name__ == '__main__':
    solve()