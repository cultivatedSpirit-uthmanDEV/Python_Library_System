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


## Available Book in the library

def available_book():
   for Avail_Book in Books:
    print("Available Book: " f"{Avail_Book['title']} by ({Avail_Book['author']}) ({Avail_Book['year']})")


available_book()






  

