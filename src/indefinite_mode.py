from src.file_splitter import *

BACK_ACTION = "back"


def indefinite_mode(quasar_spectrum):
    try:
        keep_adding = True
        while keep_adding:
            min_wavelength = input("Enter the minimum wavelength or \"%s\" "
                                   "to go back to the option menu: " % BACK_ACTION)
            if min_wavelength == BACK_ACTION:
                return None
            min_wavelength = float(min_wavelength)
            if min_wavelength < quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]:
                min_wavelength = quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]
            max_wavelength = input("Enter the maximum wavelength: ")
            max_wavelength = float(max_wavelength)
            if max_wavelength > quasar_spectrum[len(quasar_spectrum) - 1][WAVELENGTH_TUPLE_INDEX]:
                max_wavelength = quasar_spectrum[len(quasar_spectrum) - 1][WAVELENGTH_TUPLE_INDEX]
            elif max_wavelength < quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]:
                return "Maximum must be in the range of the spectrum!"
            elif max_wavelength == min_wavelength:
                return "Maximum cannot equal the minimum!"
            elif max_wavelength < min_wavelength:
                return "Maximum must be greater than the minimum wavelength!"
            directory = get_directory(min_wavelength, max_wavelength, True)
            working_segment = segment_file(quasar_spectrum, min_wavelength, max_wavelength)
            make_file_indefinitely(directory, working_segment, min_wavelength, max_wavelength)
            print("File successfully created!")
    except ValueError:
        return "Input error. Not a valid number"

    return None
