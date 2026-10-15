class Publication():
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def get_title(self):
    return self.title

  def get_author(self):
    return self.author

  def display_about_Publication(self):
    print("Publication information: ")
    print("Author: ", self.author)
    print("Title: ", self.title)
    print(" ")
    

class book(Publication):
  def __init__(title, author, number_of_pages):
    self.title = title
    self.author = author
    self.number_of_pages = number_of_pages

  def display_about_book(self):
    print("Book Information: ")
    print("Title:", self.title)
    print("Author:", self.author)
    
class magazine(Publication):
  pass

yes = Publication("Pride and Prejeduce", "Jane Austen")
yes.display_about_Publication


 
