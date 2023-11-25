class Library:
    def __init__(self):
        self.books = []
        self.totalBooks = 0
    
    @property
    def Details(self):
        print("total no. of books in library : ",self.totalBooks)
        if self.totalBooks > 0:
            user_input = input("enter yes if wanna see the list of books in library : ")
            if user_input == 'yes':
                print("the list of books is here :-")
                for i in self.books:
                    print(i)
    
    @property
    def bookAdd(self):
        None
    
    @bookAdd.setter
    def bookAdd(self,bookName):
        self.books.append(bookName)
        self.totalBooks = len(self.books)
      
      
        
lib1 = Library()
lib1.Details
def userBookAdd():
    user_wish = input("Enter yes if you wanna add books in library : ")
    if user_wish == 'yes':
        total = int(input("total no. of books you wanna add : "))
        for i in range(1,total+1):
            bookEntry = input(f"Book {i} : ")
            lib1.bookAdd = bookEntry
        print("\nall book added successfully\n")
userBookAdd()
lib1.Details