from heading import print_title
from message import book_found_msg, book_not_found_msg


def print_update(books):
    found = False
    print_title("Update a Book")

    search_book_name = input("Enter Book Name: ")

    for book in books:
        if search_book_name == book["name"]:
            found = True
            book_found_msg()

            update_qty = int(input("Enter Update Quantity: "))
            inventory_qty = book["qty"]

            if update_qty > 0:
                book["qty"] = inventory_qty + update_qty
            break

    if not found:
        book_not_found_msg()
