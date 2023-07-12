import csv
class Borrower():
    def __init__(self, user_name, phone, email, address, city,zip, membership_id ):
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.zip =zip
        self.membership_id = membership_id

    def add_borrower(self):
        book_data = f"{self.user_name},{self.phone},{self.email},{self.address},{self.city},{self.zip},{self.membership_id}\n"
        found = self.search_borrower_by_membership_id(self.membership_id)
        if not found:
            with open("borrower_data.csv", "a+") as file:
                file.write(book_data)
            print('-------------------------------')
            print("Borrower added successfully!")
            print('-------------------------------')
        else:
            print('-------------------------------')
            print("Borrower already exists!!!")
            print('-------------------------------')

    def search_borrower_by_membership_id(self, membership_id):
        found = False
        with open("borrower_data.csv", "r") as file:
            for line in file:
                borrower_info = line.strip().split(",")
                if borrower_info[6] == membership_id:
                    found = True
                    return found
            if not found:
                return found
            
    def update_borrower(self, membership_id, updated_data):
        with open("borrower_data.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open("borrower_data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(rows[0])  # Write the header row
                for row in rows[1:]:
                    if row[6] == membership_id:
                        writer.writerow(updated_data)
                    else:
                        writer.writerow(row)
        print('-------------------------------')
        print("Borrower updated successfully!")
        print('-------------------------------')
    
