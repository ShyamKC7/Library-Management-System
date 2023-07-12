import csv
class Transaction:
    def __init__(self, book, member_id, borrow_date, expected_return_date, actual_return_date):
        self.book = book
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.expected_return_date = expected_return_date
        self.actual_return_date = actual_return_date

    #Record the transaction in a csv file
    def record_transaction(self):
        transaction_data = [self.book, self.member_id, self.borrow_date, self.expected_return_date, self.actual_return_date]
        with open('transaction_data.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow(transaction_data)
            print("You have successfully Borrowed a Book")
            #After Borrowed Successfully, Decrease Qantity on book data
            # Decrease quantity in book_data.csv by 1
        with open('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row[2] == self.book:
                if int(row[4]) > 0:
                    row[4] = str(int(row[4]) - 1)
                    break
            
        with open('book_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            print("Quantity updated successfully!")
       
