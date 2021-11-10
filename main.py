# implement a student library system using oops where students can borrow a book from the list of books.
# create a separate library and student class.
# your program must be menu driven.
# you are free to choose methods and attributes of your choice to implement this functionality.

class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("books present in this library are: ")
        for book in self.books:
            print("\t * " + book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("sorry, this book is either not available or has already been issued to someone else. please wait until the book is available")
            return False
    
    def returnbook(self, bookname):
        self.books.append(bookname)
        print("thanks for returning this book ! hope you enjoyed reading it.")


class student:
    def requestbook(self):
        self.books = input("enter the name of the book you want to borrow : ")
        return self.books

    def returnbook(self):
        self.book = input("enter the name of the book you want to return : ")
        return self.book

if __name__ == "__main__":
    centralibrary = library(["algorithms","django","clrs","python"])
    student = student()
    while(True):
        welcomemsg = ''' 
        ********** WELCOME TO CENTRAL LIBRARY **********
        please choose an option:
        1. list all the books
        2. request a book
        3. add/return a book
        4. exit the library
        '''
        print(welcomemsg)

        a = int(input("enter a choice: "))
        if a == 1:
            centralibrary.displayavailablebooks()
        elif a == 2:
            centralibrary.borrowbook(student.requestbook())
        elif a == 3:
            centralibrary.returnbook(student.returnbook())
        elif a == 4:
            print("thanks for choosing central library. have a gret day ahead!")
            exit()
        else:
            print("invalid choice!")

        

        

