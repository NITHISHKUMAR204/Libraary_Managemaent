from Libraary_Managemaent_Function import *

list_names=["A","B","C","D","E","F","G"]

lib=Library(list_names)
print("Welcome to Library ,Enter an option")
while True:
    print("1.Display all books ")
    print("2.Display available books ")
    print("3.borow a book ")
    print("4.Return a book ")
    print("5.Quit")

    user_choice=int(input("Enter an option :"))

    if user_choice==1:
        lib.display_all_book()
        
    elif user_choice==2:
        lib.available_book()
                                  
    elif user_choice==3:
       user_name=input("Enter Your Name :")
       user_book=input("Enter a Book Name :")
       lib.land_book(user_name,user_book.upper())
    elif user_choice==4:
        user_book=input("Enter a Book Name :")
        lib.return_book(user_book.upper())
    elif user_choice==5:
        print("Tank You !")
        break
    else:
        print("Invalid choice")


