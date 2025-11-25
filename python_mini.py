# HEADING

print("      ")
print("      ")
print("LIBRARY MANAGEMENT SYSTEM")
print("      ")

## add book to library

Books = []

def add_book(title, author, year):
  Book = {'title' : title, 'author' : author,'year' : year}
  Books.append(Book)
  print(f"Book '{title}' added to library.")

add_book( title= "The journey to west", author= "J. Uthman", year= "1956")
  

