## Library Management

    
class Library():
    def __init__(self,list_name):
        self.book_list=list_name
        self.available_book_list=list_name[:]
        self.book_lant={}

    def display_all_book(self):
        print("Display all books.... ")
        for i in self.book_list:
            print(i)
    def available_book(self):
        print("Display available books ....")
        for i in self.available_book_list:
            print(i)

    def land_book(self,name,book):
        if book not in self.book_list:
            print("Incorrect book name. Place Cheak book list")
            return
        if book in self.available_book_list:
            self.book_lant.update({book:name})
            self.available_book_list.remove(book)
            print("You can take the book")
        else:
            print("The book is already taken by "+self.book_lant[book])

    def return_book(self,book):
        if book in self.book_list:
            if book not in  self.available_book_list:
                del self.book_lant[book]
                self.available_book_list.append(book)
            else:
                print("Ronk Book.....")
        else:
            print("Invalid Book........")
        






