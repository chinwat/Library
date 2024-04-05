from datetime import datetime, timedelta 
 
class Member: 
    def __init__(self, name, member_id, contact_info): 
        self.name = name 
        self.member_id = member_id 
        self.contact_info = contact_info 
 
class Publication: 
    def __init__(self, title, author, year): 
        self.title = title 
        self.author = author 
        self.year = year 
 
    def additional_info(self): 
        pass 
 
class Book(Publication): 
    def __init__(self, title, author, year, isbn, book_type): 
        super().__init__(title, author, year) 
        self.isbn = isbn 
        self.book_type = book_type 
 
    def additional_info(self): 
        return f"ISBN: {self.isbn}, Type: {self.book_type}" 
 
class Loan: 
    def __init__(self, member, publication, borrow_date, due_date): 
        self.member = member 
        self.publication = publication 
        self.borrow_date = borrow_date 
        self.due_date = due_date 
 
class Library: 
    def __init__(self): 
        self.members = [] 
        self.publications = [] 
        self.loans = [] 
 
    def add_member(self, member): 
        self.members.append(member)
    def find_member(self, member_id): 
        for member in self.members: 
            if member.member_id == member_id: 
                return member 
        return None 
 
    def display_member_details(self, member): 
        print(f"Name: {member.name}") 
        print(f"Member ID: {member.member_id}") 
        print(f"Contact Info: {member.contact_info}") 
 
    def add_publication(self, publication): 
        self.publications.append(publication) 
 
    def find_publication(self, title): 
        for pub in self.publications: 
            if pub.title == title: 
                return pub 
        return None 
 
    def display_publication_details(self, publication): 
        print(f"Title: {publication.title}") 
        print(f"Author: {publication.author}") 
        print(f"Year: {publication.year}") 
        print(publication.additional_info()) 
 
    def borrow_publication(self, member, publication, borrow_date, due_date): 
        if publication in self.publications: 
            self.loans.append(Loan(member, publication, borrow_date, due_date)) 
            return True 
        else: 
            return False 
 
    def is_book_overdue(self, book): 
        for loan in self.loans: 
            if loan.publication == book: 
                due_date = datetime.strptime(loan.due_date, '%Y-%m-%d') 
                if datetime.now() > due_date: 
                    return True 
        return False 
 
    def display_overdue_books(self): 
        overdue_books = [] 
        for loan in self.loans: 
            due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')
            if datetime.now() > due_date: 
                overdue_books.append(loan.publication) 
         
        if overdue_books: 
            print("Overdue Books:") 
            for book in overdue_books: 
                print(f"- {book.title} by {book.author}") 
        else: 
            print("No overdue books found.") 
 
    def display_loan_details(self, member): 
        loans = [loan for loan in self.loans if loan.member == member] 
        if loans: 
            print("Loan Details:") 
            for loan in loans: 
                print(f"Publication: {loan.publication.title}") 
                print(f"Borrow Date: {loan.borrow_date}") 
                print(f"Due Date: {loan.due_date}") 
        else: 
            print("No loans found for this member.") 
 
def add_new_member(library): 
    name = input("Enter member's name: ") 
    member_id = input("Enter member ID: ") 
    contact_info = input("Enter contact information: ") 
    new_member = Member(name, member_id, contact_info) 
    library.add_member(new_member) 
    print("New member added successfully.") 
 
def search_member(library): 
    member_id = input("Enter member ID: ") 
    member = library.find_member(member_id) 
    if member: 
        library.display_member_details(member) 
    else: 
        print("Member not found.") 
 
def add_new_book(library): 
    title = input("Enter book title: ") 
    author = input("Enter author: ") 
    year = input("Enter year of publication: ") 
    isbn = input("Enter ISBN: ") 
    book_type = input("Enter book type: ") 
    new_book = Book(title, author, year, isbn, book_type) 
    library.add_publication(new_book)
    print("New book added successfully.") 
 
def search_book(library): 
    title = input("Enter book title: ") 
    book = library.find_publication(title) 
    if book: 
        library.display_publication_details(book) 
    else: 
        print("Book not found.") 
 
def borrow_book(library): 
    member_id = input("Enter member ID: ") 
    member = library.find_member(member_id) 
    if not member: 
        print("Member not found.") 
        return 
 
    title = input("Enter book title to borrow: ") 
    book = library.find_publication(title) 
    if not book: 
        print("Book not found.") 
        return 
 
    borrow_date = datetime.now().strftime('%Y-%m-%d') 
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')  # เพมระยะเวลำยืม 14 วัน 
    if library.borrow_publication(member, book, borrow_date, due_date): 
        print("Book borrowed successfully.") 
    else: 
        print("Book is not available for borrowing.") 
 
def display_loan_details(library): 
    member_id = input("Enter member ID: ") 
    member = library.find_member(member_id) 
    if member: 
        library.display_loan_details(member) 
    else: 
        print("Member not found.") 
 
def main(): 
    library = Library() 
    while True: 
        print("\nLibrary Management System") 
        print("1. Add New Member") 
        print("2. Search Member")
        print("3. Add New Book") 
        print("4. Search Book") 
        print("5. Borrow Book") 
        print("6. Display Loan Details") 
        print("7. Display Overdue Books")  # เพมเมนน 
        print("8. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == '1': 
            add_new_member(library) 
        elif choice == '2': 
            search_member(library) 
        elif choice == '3': 
            add_new_book(library) 
        elif choice == '4': 
            search_book(library) 
        elif choice == '5': 
            borrow_book(library) 
        elif choice == '6': 
            display_loan_details(library) 
        elif choice == '7': 
            library.display_overdue_books()  # เรียกใช้ฟังก์ชัน display_overdue_books() 
        elif choice == '8': 
            print("Exiting program.") 
            break 
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == "__main__": 
    main()