class library:
    def __init__(self,books):
        self.books=books
    #list the books
    def list_books(self):
        print("Available books:")
        for book in self.books:
            print(book)
            
    #take the book to library
    def barrow_book(self,b_book):
        if b_book in self.books:
            print("Get your book now")
            self.books.remove(b_book)
        else:
            print("Not available for book in library")
            
    #return the book for libarary
    def receive_book(self,r_book):
        print("You have returned the book")
        self.books.append(r_book)
        
books=['c','c++','python','java']
o=library(books)
msg="""
     1.list books
     2.barrow books
     3.receive books
"""
while True:
    print("WELCOME TO AJAY LIBRARY...")
    print(msg)
    ch=int(input("Enter your choice :"))
    if ch==1:
        o.list_books()
        
    elif ch==2:
        book=input("you have the book name:")
        o.barrow_book(book)
        
    elif ch==3:
        b=input("Enter the book name for return:")
        o.receive_book(b)
    else:
        print("Thank you learn for book")
        quit()