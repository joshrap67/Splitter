from src.definite_mode import *
from src.indefinite_mode import *
import os

DEFINITE_MODE = "0"
INDEFINITELY_MODE = "1"
HELP_MODE = "h"
QUIT = "q"


def main():
    print("\t**********************************************")
    print("\t***     Wavelength-Flux Splitter           ***")
    print("\t**********************************************")

    print('Note that this program expects a space delimited text file with two columns,'
          '\nand the first column corresponding to wavelength (float) and the second to flux (float).\n')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    text_files = dict()
    text_file_count = 0
    for f in files:
        # only list the text files in the current directory
        filename, file_extension = os.path.splitext(f)
        if file_extension == ".txt":
            text_files[str(text_file_count)] = f
    text_file_list = ""
    for k, v in text_files.items():
        text_file_list += "%s: %s\n" % (k, v)
    text_file_list.strip()

    raw_input = input("Enter the file name (.txt extension not required) or "
                      "type number corresponding to the file you wish to segment\n%s"
                      % text_file_list)
    input_file = ""
    if raw_input in text_files or (("%s.txt" % raw_input) in files):
        input_file = text_files[raw_input]
    elif ("%s.txt" % raw_input) in files:
        input_file = "%s.txt" % raw_input
    else:
        print("File not found!")
        quit()

    os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal input
    quasar_spectrum = read_file(input_file)
    # in case the file is not sorted correctly
    quasar_spectrum.sort(key=lambda d: d[WAVELENGTH_TUPLE_INDEX])  # sort based on wavelength

    keep_running = True
    while keep_running:
        decision = input("Enter:\n"
                         "\"%s\" to create a definite number of files from a set range and overlap\n"
                         "\"%s\" to create individual files\n"
                         "\"%s\" to get a summary of the options for the app\n"
                         "\"%s\" to exit the program\n"
                         % (DEFINITE_MODE, INDEFINITELY_MODE, HELP_MODE, QUIT))
        if decision == DEFINITE_MODE:
            return_msg = definite_mode(quasar_spectrum)
            print(return_msg)
        elif decision == INDEFINITELY_MODE:
            return_msg = indefinite_mode(quasar_spectrum)
            if return_msg is not None:
                print(return_msg)
        elif decision == HELP_MODE:
            print("help")
        elif decision == QUIT:
            keep_running = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal input
            print("Invalid Action!")
    os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal input
    quit()


if __name__ == "__main__":
    main()
