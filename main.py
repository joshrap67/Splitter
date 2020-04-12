from src.definite_mode import *
from src.indefinite_mode import *

DEFINITE = "d"
INDEFINITELY = "i"
NEW_FILE = "f"
QUIT = "q"


def main():
    """
    Main method of the program. It prompts the user to input a file either by name or
    using an index corresponding to a file in a dictionary.

    If the file exists, start the program loop.

    :return: None
    """
    print('Note that this program expects a space delimited .txt file with two columns,'
          '\nand the first column corresponding to wavelength (float) and the second to flux (float).\n')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]  # all files in current directory
    text_files = dict()  # map of unique_index -> file_name
    text_file_count = 0
    for f in files:
        # only list the text files in the current directory
        filename, file_extension = os.path.splitext(f)
        if file_extension == ".txt":
            text_files[str(text_file_count)] = f
            text_file_count += 1
    text_file_list = ""
    for k, v in text_files.items():
        text_file_list += "%s: %s\n" % (k, v)
    text_file_list.strip()

    raw_input = input("Enter the file name or "
                      "type number corresponding to the file you wish to segment\n%s"
                      % text_file_list)
    input_file = ""
    if raw_input in text_files:
        input_file = text_files[raw_input]
    elif raw_input in files:
        input_file = raw_input
    else:
        print("File not found!")
        quit()

    clear_output()
    quasar_spectrum = read_file(input_file)
    # in case the file is not sorted correctly
    quasar_spectrum.sort(key=lambda d: d[WAVELENGTH_TUPLE_INDEX])  # sort based on wavelength
    program_loop(quasar_spectrum)


def program_loop(quasar_spectrum):
    """
    Provides a loop for the user to constantly pick different actions to execute.

    :param quasar_spectrum: a list of tuples. Covers every point in original file (wavelength,flux)
    :return: None
    """
    keep_running = True
    while keep_running:
        decision = input("Enter:\n"
                         "\"%s\" to create a definite number of files from a given range and overlap\n"
                         "\"%s\" to create individual files\n"
                         "\"%s\" to load a new file\n"
                         "\"%s\" to exit the program\n"
                         % (DEFINITE, INDEFINITELY, NEW_FILE, QUIT))
        if decision == DEFINITE:
            clear_output()
            return_msg = definite_mode(quasar_spectrum)
            print(return_msg)
        elif decision == INDEFINITELY:
            clear_output()
            return_msg = indefinite_mode(quasar_spectrum)
            if return_msg is not None:
                print(return_msg)
        elif decision == NEW_FILE:
            main()
            keep_running = False
        elif decision == QUIT:
            keep_running = False
            clear_output()
            quit()
        else:
            clear_output()
            print("Invalid Action!")


def clear_output():
    """
    Clears the most recent output of the interpreter.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal input


if __name__ == "__main__":
    print("\t**********************************************")
    print("\t***     Wavelength-Flux Splitter           ***")
    print("\t**********************************************")
    main()
