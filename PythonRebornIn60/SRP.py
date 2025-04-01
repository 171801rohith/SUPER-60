class UserManager:
    def create_user(self, username, password):
        # Save user to database
        print(f"User {username} created.")

    def authenticate(self, username, password):
        # Check credentials
        print(f"User {username} authenticated.")

    def send_welcome_email(self, username):
        # Send email
        print(f"Welcome email sent to {username}.")


class Create_User:
    def create_user(self, username, password):
        # Save user to database
        print(f"User {username} created.")


class Authenticator:
    def authenticate(self, username, password):
        print(f"User {username} authenticated.")


class Email:
    def send_welcome_email(self, username):
        # Send email
        print(f"Welcome email sent to {username}.")


# Design classes for: Managing books (adding/removing). Borrowing books. Generating reports.


class BookManager:
    def addBook(self, book_title):
        print(f"{book_title} added.")

    def removeBook(self, book_title):
        print(f"{book_title} removed.")


class BorrowBook:
    def borrowBook(self, username, book_title):
        print(f"{book_title} borrowed by {username}")

    def returnBook(self, username, book_title):
        print(f"{book_title} returned by {username}")


class GenerateReport:
    def generateReport(self):
        print("Report Generated.")


class DiscountCalculator:
    def calculate_discount(self, customer_type, price):
        if customer_type == "Standard":
            return price * 0.1  # 10% discount
        else:
            return 0  # No discount for others