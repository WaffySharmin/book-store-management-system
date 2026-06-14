from menu import print_menu
from message import closing_msg
from heading import print_title
from create import print_create
from list import print_list
from sell import print_sell
from update import print_update
from delete import print_delete

books = []

while True:
    print_menu()

    user_input = int(input("Enter your choice: "))

    if user_input == 0:
        closing_msg()
        break

    if user_input == 1:
        keep_running = print_create(books)
        if not keep_running:
            break

    if user_input == 2:
        keep_running = print_list(books)
        if not keep_running:
            break

    if user_input == 3:
        keep_running = print_sell(books)
        if not keep_running:
            break

    if user_input == 4:
        print_update(books)

    if user_input == 5:
        print_delete(books)
