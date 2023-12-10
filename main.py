import util

choice = 0

while choice != 6:
    util.display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        util.display_all_movies()
    elif choice == 2:
        util.display_top_10_rows()
    elif choice == 3:
        util.display_last_10_rows()
    elif choice == 4:
        util.find_shape_of_dataset()
    elif choice == 5:
        util.display_top_10_highest_rated_movies()
