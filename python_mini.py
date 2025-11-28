class library():
  def __init__(self):
    self.Books = []
  ## Add book to library

  def add_Book(self,title,author,year):
    Book = {
      "title" : title,
      "author" : author,
      "year" : year}
    self.Books.append(Book)
    print(f"'{title}' has been added")

    ## check available book

  def avail_Book(self):
    for Book in self.Books:
      print(f"{Book['title']} by {Book['author']}({Book['year']})")
   ##  search for book
  def search_book(self,title):
    for Book in self.Books:
      if Book['title'] == title:
        print(f"{Book['title']} by {Book['author']} in {Book['year']} Found!")
      return
  print('Not Found!')

  ## Borrow book

  def borrow_Book(self,title):
    for Book in self.Books:
      if Book['title'] == title:
        self.Books.remove(Book)
        print(f"{Book['title']} by {Book['author']} has been borrowed out")
        return
    print("Book not found")






lib = library()
lib.add_Book("Python for beginners", "NoorLab institute", "2025")
lib.add_Book("The journey to west", "J. chenyu", "1956")
lib.add_Book("futurist peeps", "W. Uthman", "1956")

print("      ")
print("      ")
print("      ")
print("      ")
lib.avail_Book()

print("      ")
print("      ")


lib.search_book("Python for beginners")
print("      ")
lib.borrow_Book("The journey to west")


    