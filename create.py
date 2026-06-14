from heading import print_title
from message import back_or_exit, closing_msg


def print_create(books):
    print_title("Create new book")

    book_name = input("Enter Book Name: ")
    book_qty = int(input("Enter Initial Book Quantity: "))

    new_book = {"name": book_name, "qty": book_qty}
    books.append(new_book)

    print(f"Book Name: {book_name} Successfully Added")
    back_or_exit()

    user_input = int(input("Enter your choice: "))
    if user_input == 0:
        closing_msg()
        return False
    return True
