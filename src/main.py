import text_analyzer
import number_analyzer
import search_sort
import file_manager
def display_menu():
    print("\n===== MAIN MENU =====")
    print("1. NUMBER ANALYZER")
    print("2. TEXT ANALYZER")
    print("3. SEARCH AND SORT")
    print("4. FILE MANAGER")
    print("5. EXIT")
def get_user_choice():
    while True:
        try:
            choice = int(input("What operation would you like to do?"))
            break
        except ValueError:
            print("Wrong input.\nEnter an integer value.")
    return choice
def handle_choice(choice):
    if choice == 1:
        number_analyzer.main()
        return True
    elif choice == 2:
        text_analyzer.main()
        return True
    elif choice == 3:
        search_sort.main()
        return True
    elif choice == 4:
        file_manager.main()
        return True
    elif choice == 5:
        return False
    else:
        print("Invalid choice")
        return True
def main():
    while True: 
        display_menu()
        choice = get_user_choice()
        result = handle_choice(choice)

        if not result:
            break
if __name__ == "__main__":
    main()

            





     
            