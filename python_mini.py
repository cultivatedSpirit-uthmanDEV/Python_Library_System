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

add_book( title= "Python for begonners", author= "NoorLab institute", year= "2025")
add_book( title= "The journey to west", author= "J. chenyu", year= "1956")
add_book( title= "futurist peeps", author= "W. Uthman", year= "1956")


## Available Book in the library

print("      ")
print("      ")
print("Available Book in the library")
print("      ")



def available_book():
   for Avail_Book in Books:
    print("Available Book: " f"{Avail_Book['title']} by ({Avail_Book['author']}) ({Avail_Book['year']})")


available_book()

## Book search

print("      ")
print("      ")
print("Book Search")
print("      ")



def search_book(title):
  for Book in Books:
    if Book['title'].lower() == title.lower():
      print(f"Found: {Book['title']} by {Book['author']} ({Book['year']})")
      return
  print("Book not found")

search_book( "futurist peeps")


## Borrowed book

print("      ")
print("      ")
print("Borrow Book")
print("      ")


def borrow_Book(title):
  for Book in Books:
    if Book['title'].lower() == title.lower():
      Books.remove(Book)
      print(f"{Book['title']} has been borrowed out")
      return
  print('Book not found')


borrow_Book('The journey to west')





  

