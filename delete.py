from heading import print_title
from message import book_found_msg, book_not_found_msg


def print_delete(books):
    found = False
    print_title("Delete")

    search_book_name = input("Enter book name: ")

    for book in books:
        if search_book_name == book["name"]:
            found = True
            book_found_msg()

            delete_qty = int(input("Enter delete Quantity: "))

            if 0 < delete_qty <= book["qty"]:
                book["qty"] -= delete_qty
                print("Quantity deleted successfully.")
            else:
                print("Invalid quantity")
            break

    if not found:
        book_not_found_msg()
