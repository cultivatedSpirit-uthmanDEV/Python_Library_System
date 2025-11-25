# HEADING

print("      ")
print("      ")
print("LIBRARY MANAGEMENT SYSTEM")
print("      ")

## add book to library

Books = []

def add_book(title, author, year):
  Book = {
    'title' : title, 'author' : author,  
    'year' : year}
  Books.append(f"The Book' {title}', by {author}, {year} added to the library.")
  print(Books)

add_book(title= " The journey to west ", author=" F. Uthman ",  year=1902)
  

