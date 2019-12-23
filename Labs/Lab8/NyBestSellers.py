def create_books_2Dlist(file_name):
    """(str) -> list of list of str
    Returns a 2D list containing books and their information from a file.
    The list will contain the information in the format:
    Publication date(YYYY-MM-DD), Title, Author, Publisher, Genre.
    Preconditions: each line in the file specified contains information about
    a book. In the format Title, Author, Publisher, Publication date(DD/MM/YY),
    Genre.
    """
    ny = open(file_name).read().splitlines()
    ny_table =[]

    for book in ny:
        book = book.split("\t")
        name = book[0].strip()
        author = book[1].strip()
        publisher = book[2].strip()
        date = book[3].strip()
        genre = book[4].strip()
        ny_table.append([date, name, author, publisher, genre])

    return ny_table
def search_by_year(books, year1, year2):
    """(list of list of str, int, int)
    Prints a list of books in the list books published
    between year1 and year2.

    Precondition: books is a list created from create_books2Dlist
    """
    book_list = []
    for i in range(len(books)):
            if books[i][0][-4:] >= year1 and books[i][0][-4:]<= year2:
                book_list.append(books[i])
    return book_list
            
            

#main
file_name = input("Enter the name of the file: ")
file_name = file_name.strip()
ny_table = create_books_2Dlist(file_name)
print(ny_table)
print("-----")
print(search_by_year(ny_table, "1980", "2005"))
