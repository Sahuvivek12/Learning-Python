# Library management system


class Library:
    books = []
    def AddBooks(self, int):
        total = sum(self.books)
        self.books.append(int)
        print(self.books)
        print(len(self.books))
    def RemoveBooks(self, int):
        self.books.remove(int)
        print(self.books)
        
        
a = Library() 

a.AddBooks(9)
a.AddBooks(88)