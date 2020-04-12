import os
from pathlib import Path

WAVELENGTH_TUPLE_INDEX = 0
FLUX_TUPLE_INDEX = 1
COLUMN_COUNT = 2


def read_file(file_name):
    """
    Reads a space delimited .txt file and produces a list of data.

    :param file_name: name of file to read from (string)
    :return: a list of tuples. Covers every point in original file (wavelength,flux)
    """
    if file_name is None:
        return None
    try:
        ret_val = list()
        working_file = open(file_name, 'r')
        for line in working_file:
            line = line.rstrip()
            split_lines = line.split()  # delimeter is a space character
            if not len(split_lines) == COLUMN_COUNT:
                print('File not formatted correctly')
                quit()
            wavelength = float(split_lines[WAVELENGTH_TUPLE_INDEX])
            flux = float(split_lines[FLUX_TUPLE_INDEX])
            data_tuple = (wavelength, flux)
            ret_val.append(data_tuple)
        return ret_val
    except FileNotFoundError:
        return None


def segment_spectrum(quasar_spectrum, min_wavelength, max_wavelength):
    """
    Segments the spectrum of the quasar. I.e. if quasar has wavelength from 5000 to 200000
    and the min_wavelength param is 6000 and max_wavelength is 7000, then it returns a segment
    of wavelength 6000-7000.

    Note that the values are floats so in the above example the segment would include a point such as
    7000.540 and 6000.234

    :param quasar_spectrum: a list of tuples. Covers every point in original file (wavelength,flux)
    :param min_wavelength: the minimum data point for the segment (float)
    :param max_wavelength: the maximum data point for the segment (float)
    :return: a list of tuples (wavelength,flux)
    """
    segmented_spectrum = list()
    for data in quasar_spectrum:
        if (data[WAVELENGTH_TUPLE_INDEX] >= min_wavelength) and (data[WAVELENGTH_TUPLE_INDEX] < max_wavelength + 1):
            segmented_spectrum.append(data)
    return segmented_spectrum


def get_directory(min_wavelength, max_wavelength, indefinite_mode, range_spectrum=None, overlap=None):
    """
    Creates the appropriate output directories. There is a base output directory and then indefinite
    files created are added to this and any files made in definite mode are put into a separate
    folder within the output one.

    Definite folder naming format: <min_wavelength>_<max_wavelength>_<range_spectrum>_<overlap>

    :param min_wavelength: the minimum data point for the segment (float)
    :param max_wavelength: the maximum data point for the segment (float)
    :param indefinite_mode: true if making files indefinitely (bool)
    :param range_spectrum: optional parameter for definite mode specifying the range of the files (int)
    :param overlap: optional parameter for definite mode specifying the overlap of the files (int)
    :return: the base directory to write files in (string)
    """
    minimum = int(min_wavelength)
    maximum = int(max_wavelength)
    #  make an output folder if it doesn't already exist
    output_path = Path(os.getcwd() + "/output/")
    output_path.mkdir(parents=True, exist_ok=True)
    directory_name = output_path
    if not indefinite_mode:
        #  make a specific folder for the splitting if it is in definite mode
        directory_name = Path(str(output_path) + "/%s_%s_%s_%s/" % (minimum, maximum, range_spectrum, overlap))
        directory_name.mkdir(parents=True, exist_ok=True)
    return directory_name


def make_file(directory, segment, min_wavelength, max_wavelength):
    """
    Creates a .txt file with the given segment.

    File naming format: <min_wavelength>_<max_wavelength>

    :param directory: base directory to write the file to (string)
    :param segment: the segment to write to the file (list of tuples)
    :param min_wavelength: the minimum data point for the segment (float)
    :param max_wavelength: the maximum data point for the segment (float)
    :return: None
    """
    minimum = int(min_wavelength)
    maximum = int(max_wavelength)
    try:
        file_name = Path(directory / ("%s_%s.txt" % (minimum, maximum)))
        output = open(str(file_name), "w")
        for i in range(0, len(segment), 1):
            if i is None:
                break
            unformatted_wavelength = segment[i][WAVELENGTH_TUPLE_INDEX]
            unformatted_flux = segment[i][FLUX_TUPLE_INDEX]
            formatted_wavelength = "{0:.6f}".format(unformatted_wavelength)  # 6 digits after decimal point
            formatted_flux = "{0:.6f}".format(unformatted_flux)  # 6 digits after decimal point
            # last line of file can't have a new line char
            output.write("%s %s\n" % (formatted_wavelength, formatted_flux) if (i != len(segment) - 1)
                         else "%s %s" % (formatted_wavelength, formatted_flux))
        output.close()
    except FileNotFoundError:
        print("Error. Cannot write to file.")
