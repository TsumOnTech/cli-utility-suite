import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")


def get_filepath(filename):
    data_real = os.path.realpath(DATA_DIR)
    filepath = os.path.realpath(os.path.join(data_real, filename))
    if os.path.commonpath([data_real, filepath]) != data_real or filepath == data_real:
        return None
    return filepath


def create_file(filename):
    filepath = get_filepath(filename)
    if filepath is None:
        return False
    try:
        with open(filepath, "x") as file:
            result = True
            return result
    except FileExistsError:
        result = False
        return result


def write_file(filename, text):
    filepath = get_filepath(filename)
    if filepath is None or not os.path.exists(filepath):
        result = False
        return result
    try:
        with open(filepath, "w") as file:
            file.write(text + "\n")
            result = True
            return result
    except FileNotFoundError:
        result = False
        return result


def read_file(filename):
    filepath = get_filepath(filename)
    if filepath is None:
        return None
    try:
        with open(filepath, "r") as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return None


def append_file(filename, text):
    filepath = get_filepath(filename)
    if filepath is None or not os.path.exists(filepath):
        result = False
        return result
    try:
        with open(filepath, "a") as file:
            file.write(text + "\n")
            result = True
        return result
    except FileNotFoundError:
        result = False
        return result


def delete_file(filename):
    filepath = get_filepath(filename)
    if filepath is None:
        return False
    try:
        os.remove(filepath)
        result = True
        return result
    except FileNotFoundError:
        result = False
        return result


def file_information(filename):
    filepath = get_filepath(filename)
    if filepath is None:
        return None
    file_infos = {}
    try:
        file_infos["File name"] = filename
        with open(filepath, "r") as file:
            lines = file.readlines()
            file_infos["lines"] = len(lines)

        result = os.path.getsize(filepath)
        file_infos["The size of the file"] = result
        return file_infos
    except FileNotFoundError:
        return None


def validate_filename(filename):
    if "/" in filename or "\\" in filename or ".." in filename:
        return False
    if filename.lower().endswith(".txt") and len(filename) > 4:
        return True
    return False


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    while True:
        print("\n===== FILE MANAGER TOOLKIT =====")
        print("1. CREATE FILE")
        print("2. WRITE FILE")
        print("3. READ FILE")
        print("4. ADD FILE")
        print("5. DELETE FILE")
        print("6. FILE INFORMATION")
        print("7. EXIT")
        try:
            choice = int(input("What operation would you like to proceed with?: "))

            if choice == 1:
                filename = input("Enter the name of the file: ")
                if validate_filename(filename):
                    result = create_file(filename)
                    if result:
                        print("File created.")
                    else:
                        print("File already exists.")
                else:
                    print("Invalid Filename. Only .txt files are allowed.")
            elif choice == 2:
                filename = input("Enter the name of the file: ")
                if validate_filename(filename):
                    text = input("Enter the text: ")
                    result = write_file(filename, text)
                    if result:
                        print("File written.")
                    else:
                        print("The File was not found.")
                else:
                    print("Invalid Filename. Only .txt files are allowed.")
            elif choice == 3:
                filename = input("Enter the name of the file: ")
                if validate_filename(filename):
                    contents = read_file(filename)
                    if contents is not None:
                        print(contents)
                    else:
                        print("The File was not found.")
                else:
                    print("Invalid Filename. Only .txt files are allowed.")
            elif choice == 4:
                filename = input("Enter the name of the file: ")
                if validate_filename(filename):
                    text = input("Enter the text: ")
                    result = append_file(filename, text)
                    if result:
                        print("Text appended.")
                    else:
                        print("The File was not found.")
                else:
                    print("Invalid Filename. Only .txt files are allowed.")
            elif choice == 5:
                filename = input("Enter the name of the file: ")
                if validate_filename(filename):
                    result = delete_file(filename)
                    if result:
                        print("File deleted.")
                    else:
                        print("The File was not found.")
                else:
                    print("Invalid Filename. Only .txt files are allowed.")
            elif choice == 6:
                filename = input("Enter the name of the file: ")
                if validate_filename(filename):
                    file_infos = file_information(filename)
                    if file_infos is not None:
                        print(file_infos)
                    else:
                        print("The File was not found.")
                else:
                    print("Invalid Filename. Only .txt files are allowed.")
            elif choice == 7:
                print("Exiting application. Thank you!")
                break
            else:
                print("Invalid Choice. \nEnter a valid choice.")

        except ValueError:
            print("Wrong value,\nTry again")


if __name__ == "__main__":
    main()