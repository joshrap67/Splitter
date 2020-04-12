from src.file_splitter import *


def definite_mode(quasar_spectrum):
    """
    Allows for a set number of segmented files to be created from a given min and max wavelength,
    a range(range of wavelengths contained in each file),
    and an overlap (how many old data points are included in subsequent files)

    :param quasar_spectrum: a list of tuples. Covers every point in original file (wavelength,flux)
    :return: None
    """
    try:
        quasar_min_wavelength = quasar_spectrum[0][WAVELENGTH_TUPLE_INDEX]
        quasar_max_wavelength = quasar_spectrum[len(quasar_spectrum) - 1][WAVELENGTH_TUPLE_INDEX]

        min_wavelength = float(input("Enter the minimum wavelength (minimum in file is %d): " % quasar_min_wavelength))
        if min_wavelength < quasar_min_wavelength:
            # user entered a wavelength lower than available, so set min to lowest wavelength in spectrum
            min_wavelength = quasar_min_wavelength
        max_wavelength = float(input("Enter the maximum wavelength (maximum in file is %d): " % quasar_max_wavelength))
        if max_wavelength > quasar_max_wavelength:
            # sets max to largest wavelength in spectrum
            max_wavelength = quasar_max_wavelength
        elif max_wavelength < quasar_min_wavelength:
            return "Maximum must be in the range of the spectrum!"
        elif max_wavelength == min_wavelength:
            return "Maximum cannot equal the minimum!"
        elif max_wavelength < min_wavelength:
            return "Maximum must be greater than the minimum wavelength!"
        range_of_spectrum = float(input("Enter the range of the spectrum: "))
        if range_of_spectrum <= 0:
            return "Range must be a positive non-zero number."
        overlap = float(input("Enter the overlap of the files: "))
        if overlap > max_wavelength:
            return "Overlap cannot be greater than the maximum wavelength!"

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
        # create all the files
        original_max = max_wavelength
        for i in range(0, files, 1):
            max_wavelength = min_wavelength + range_of_spectrum
            if max_wavelength > original_max:
                # prevents overlap from altering the inputted max wavelength.
                working_segment = segment_spectrum(quasar_spectrum, min_wavelength, original_max)
                make_file(directory, working_segment, min_wavelength, original_max)
            else:
                working_segment = segment_spectrum(quasar_spectrum, min_wavelength, max_wavelength)
                make_file(directory, working_segment, min_wavelength, max_wavelength)
            min_wavelength = max_wavelength - overlap
        return "Successfully created %s files!" % files
    except ValueError:
        return "Input error. Not a valid number!"
    except TypeError:
        return "Input error. Not a valid number!"
