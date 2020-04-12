from src.file_splitter import *

BACK_ACTION = "back"


def indefinite_mode(quasar_spectrum):
    """
    Allows for segmented files to be created indefinitely using a given min and max wavelength.

    :param quasar_spectrum: a list of tuples. Covers every point in original file (wavelength,flux)
    :return: None
    """
    try:
        quasar_min_wavelength = quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]
        quasar_max_wavelength = quasar_spectrum[len(quasar_spectrum) - 1][WAVELENGTH_TUPLE_INDEX]

        while True:
            min_wavelength = input("Enter the minimum wavelength or \"%s\" "
                                   "to go back to the option menu. (Minimum in file is %d) " % (
                                       BACK_ACTION, quasar_min_wavelength))
            if min_wavelength == BACK_ACTION:
                break
            min_wavelength = float(min_wavelength)
            if min_wavelength < quasar_min_wavelength:
                min_wavelength = quasar_min_wavelength
            max_wavelength = float(
                input("Enter the maximum wavelength (maximum in file is %d): " % quasar_max_wavelength))
            if max_wavelength > quasar_max_wavelength:
                max_wavelength = quasar_max_wavelength
            elif max_wavelength < quasar_min_wavelength:
                return "Maximum must be in the range of the spectrum!"
            elif max_wavelength == min_wavelength:
                return "Maximum cannot equal the minimum!"
            elif max_wavelength < min_wavelength:
                return "Maximum must be greater than the minimum wavelength!"
            directory = get_directory(min_wavelength, max_wavelength, True)
            working_segment = segment_spectrum(quasar_spectrum, min_wavelength, max_wavelength)
            make_file(directory, working_segment, min_wavelength, max_wavelength)
            print("File successfully created!")
    except ValueError:
        return "Input error. Not a valid number!"
    except TypeError:
        return "Input error. Not a valid number!"

    return None
