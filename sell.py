from heading import print_title
from message import back_or_exit, closing_msg, book_found_msg, book_not_found_msg


def print_sell(books):
    found = False
    print_title("Sell a Book")

    search_book_name = input("Enter Book Name: ")

    for book in books:
        if search_book_name == book["name"]:
            found = True
            book_found_msg()

            sell_qty = int(input("Enter Sell Quantity: "))
            inventory_qty = book["qty"]

            if sell_qty <= inventory_qty:
                book["qty"] = inventory_qty - sell_qty
            break

    if not found:
        book_not_found_msg()

    back_or_exit()

    user_input = int(input("Enter your choice: "))
    if user_input == 0:
        closing_msg()
        return False
    return True
