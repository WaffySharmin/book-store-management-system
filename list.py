from heading import print_title
from message import back_or_exit, closing_msg


def print_list(books):
    print_title("List of book")

    print(f"{'-' * 45}")
    print(f"|{'Book Name':^20} | {'Quantity':^20}|")
    print(f"{'-' * 45}")
    for book in books:
        print(f"|{book['name']:^20} | {book['qty']:^20}|")
        print(f"{'-' * 45}")

    back_or_exit()

    user_input = int(input("Enter your choice: "))
    if user_input == 0:
        closing_msg()
        return False
    return True
