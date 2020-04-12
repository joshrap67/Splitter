from src.file_splitter import *


def definite_mode(quasar_spectrum):
    # args: working_spectrum (entire list of tuples)
    try:
        min_wavelength = float(input("Enter the minimum wavelength: "))
        if min_wavelength < quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]:
            # user entered a wavelength lower than available, so set min to lowest wavelength in spectrum
            min_wavelength = quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]
        max_wavelength = float(input("Enter the maximum wavelength: "))
        if max_wavelength > quasar_spectrum[len(quasar_spectrum) - 1][WAVELENGTH_TUPLE_INDEX]:
            # sets max to largest wavelength in spectrum
            max_wavelength = quasar_spectrum[
                len(quasar_spectrum) - 1][WAVELENGTH_TUPLE_INDEX]
        elif max_wavelength < quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]:
            return "Maximum must be in the range of the spectrum!"
        elif max_wavelength == min_wavelength:
            return "Maximum cannot equal the minimum!"
        elif max_wavelength < min_wavelength:
            return "Maximum must be greater than the minimum wavelength!"
        range_of_spectrum = float(input("Enter the range of the spectrum: "))
        overlap = float(input("Enter the overlap of the files: "))

        # determining the number of files necessary
        files_float = ((max_wavelength - min_wavelength) / range_of_spectrum) * (1 + overlap / range_of_spectrum)
        files = 0
        if int(files_float) == files_float:
            files = int(files_float)
        else:
            # round up if the number of files is a float instead of whole number
            files = int(files_float) + 1

        directory = get_directory(min_wavelength, max_wavelength, False,
                                  range_spectrum=int(range_of_spectrum), overlap=int(overlap))
        original_max = max_wavelength
        for i in range(0, files, 1):
            max_wavelength = min_wavelength + range_of_spectrum
            if max_wavelength > original_max:
                # prevents overlap from altering the inputted max wavelength.
                working_segment = segment_file(quasar_spectrum, min_wavelength, original_max)
                make_file_definite(directory, working_segment, min_wavelength, original_max)
            else:
                working_segment = segment_file(quasar_spectrum, min_wavelength, max_wavelength)
                make_file_definite(directory, working_segment, min_wavelength, max_wavelength)
            min_wavelength = max_wavelength - overlap
        return "Successfully created %s files!" % files
    except ValueError:
        return "Input error. Not a valid number"
