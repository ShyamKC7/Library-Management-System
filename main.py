import csv
from book import Book
from borrower import Borrower
from datetime import datetime
from transaction import Transaction

def selection_validate():
    valid_selections = ('1', '2', '3', '4', '5', '6')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                          "To request a new loan enter 1 \n"
                          "To return a book enter 2 \n"
                          "To extend a loan enter 3 \n"
                          "To add a user enter 4 \n"
                          "To update a user enter 5 \n"
                          "To add a book enter 6 \n"
                          "\nEnter choice: ")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'
            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
        return selection
    
def selection_calls():
    selection = selection_validate()

    if selection == '1':
        print("You can request a book here")
        membership_id = input("Enter membership ID: ")
        borrower = Borrower(None, None, None, None, None, None, None)
        book = Book(None, None, None, None, None, None, None)
        member = borrower.search_borrower_by_membership_id(membership_id=membership_id)
        if member:
            book_title = input("Which book you want to borrow?: ")
            found = book.search_book_by_title(book_title)
            if found:
                print('***Please enter the following details ***')
                borrow_date = datetime.now().strftime("%d/%m/%y")
                expected_return_date = input("Enter return date in mm/dd/yy format: ")
                actual_return_date = input("Enter actual return date in mm/dd/yy format: ")
                burrow_book = Transaction(book=book_title, member_id=membership_id, borrow_date=borrow_date, expected_return_date=expected_return_date,actual_return_date=actual_return_date)
                burrow_book.record_transaction()
            else:
                print("Sorry we dont have this book")
        if not member:
            print('------------------------------')
            print("Member Not Found")
            print('-------------------------------')
            member_request = input("Do you want to get membership? (Yes/No) : ").lower()
            if member_request == 'yes':
                borrower.add_borrower()
            else:
                print("Thank you for your interest")

    elif selection == '2':
        print('*** You can return your book here ***\n\n')
        membership_id = input("Please enter your membership ID: ")
        borrower = Borrower(None, None, None, None, None, None, None)
        member = borrower.search_borrower_by_membership_id(membership_id=membership_id)
        #Display all the books borrowed by this membership_id
        if member:
            with open('transaction_data.csv', 'r') as file:
                found_books = []
                for line in file:
                    borrowed_details = line.strip().split(',')
                    if borrowed_details[1] == membership_id:
                        found_books.append(borrowed_details)
                if found_books:
                    print('These are the borrowed books found in our database for you:')
                    for book in found_books:
                        print(','.join(book))
                #Ask Borrower which book they want to return
                    is_return = True
                    while is_return:
                        book_to_return = input("Please enter a book title you want to return: ")
                        for book in found_books:
                            if book[0] == book_to_return:
                                #delete that row from transaction database and increase quantity on book data
                                rows = []
                                with open('transaction_data.csv', 'r') as file:
                                    reader = csv.reader(file)
                                    rows = list(reader)
                                # Remove the desired row from transaction data
                                index_value = 0
                                for i, record in enumerate(rows):
                                    if record[0] == book_to_return:
                                        index_value += i
                                        break
                                del rows[index_value]
                                # Write the modified data back to the CSV file
                                with open('transaction_data.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)
                                    
                                #add quantity to the book data after return
                                with open('book_data.csv', 'r') as file:
                                    reader = csv.reader(file)
                                    rows = list(reader)
                                    for row in rows:
                                        if row[2] == book_to_return:
                                            if int(row[4]) > 0:
                                                row[4] = str(int(row[4]) + 1)
                                                break

                                with open('book_data.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)
                                print('------------------------------')
                                print("Book returned successfully!")
                                print('-------------------------------')
                                                        
                        #ask borrower if they want to return more book
                        another_book_return = input("Do you want to return any other books(Yes/No) : ").lower()
                        if another_book_return == "no":
                            is_return = False
                else:
                    print('No borrowed books found for your membership ID.')
        else:
            print("Sorry you are not member of this library")

    elif selection == '3': #extend the date
        print('*** You can extend your book here ***\n')
        membership_id = input("Please enter your membership ID: ")
        borrower = Borrower(None, None, None, None, None, None, None)
        member = borrower.search_borrower_by_membership_id(membership_id=membership_id)
        #Display all the books borrowed by this membership_id
        
        if member:
            with open('transaction_data.csv', 'r') as file:
                found_books = []
                for line in file:
                    borrowed_details = line.strip().split(',')
                    if borrowed_details[1] == membership_id:
                        found_books.append(borrowed_details)
                if found_books:
                    print('These are the borrowed books found in our database for you:')
                    for book in found_books:
                        print(','.join(book))
                    #Ask Borrower which book they want to return
                    is_extend = True
                    while is_extend:
                        book_to_extend = input("Please enter a book title for book you want to extend: ")
                        for book in found_books:
                            if book[0] == book_to_extend:
                                new_date = input("Please enter a new return date in mm//dd/yy format: ")
                                book[3] = new_date
                                print(found_books)
                                with open('transaction_data.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(found_books)
                                print('------------------------------')
                                print("Return Date Updated successfully!")
                                print('-------------------------------')
                               
                        another_book_extend = input("Do you want to extend dates for any other books(Yes/No) : ").lower()
                        if another_book_extend == "no":
                            is_extend= False
                else:
                    print('No borrowed books found for your membership ID.')

    elif selection == '4':
        user_name = input("Enter user_name: ")
        phone = input("Enter Phone No: ")
        email = input("Enter Email: ")
        address = input("Enter address: ")
        city = input("Enter city: ")
        zip = input("Enter zip: ")
        membership_id = input("Enter Membership ID: ")
        borrower = Borrower(user_name=user_name, phone=phone, email=email, address=address, city=city, zip=zip, membership_id=membership_id)
        borrower.add_borrower()

    elif selection == '5':
        membership_id = input("Enter membership ID of the borrower to update: ")
        borrower = Borrower(None, None, None, None, None, None, None)
        found_borrower = borrower.search_borrower_by_membership_id(membership_id)
        if found_borrower:
            print("Borrower found. Enter the updated details:")
            updated_user_name = input("Enter updated User Name: ")
            updated_phone = input("Enter updated Phone Number: ")
            updated_email = input("Enter updated Email: ")
            updated_address = input("Enter updated Address: ")
            updated_city = input("Enter updated City: ")
            updated_zip = input("Enter updated Zip: ")

            updated_data = [
                updated_user_name,
                updated_phone,
                updated_email,
                updated_address,
                updated_city,
                updated_zip,
                membership_id
            ]

            borrower.update_borrower(membership_id, updated_data)
        else:
            print("Sorry Borrower Not Found !!")
       

    elif selection == '6':
        book_name = input("Enter Book Name: ")
        title = input("Enter Title: ")
        author = input("Enter author: ")
        quantity = input("Enter quantity: ")
        pub_year = input("Enter Publication Year: ")
        edition = input("Enter Edition: ")
        book_id = input("Enter Book Id: ")
        new_book = Book(book_id=book_id, book_name=book_name, title=title, author=author, quantity=quantity, pub_year=pub_year, edition=edition)
        new_book.add_book()

if __name__ == '__main__':
    selection_calls() 

    
