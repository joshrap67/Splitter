import os

WAVELENGTH_TUPLE_INDEX = 0
FLUX_TUPLE_INDEX = 1


def read_file(file_name):
    if file_name is None:
        return None
    try:
        ret_val = list()
        working_file = open(file_name, 'r')
        for line in working_file:
            line = line.rstrip()
            split_lines = line.split()
            if not len(split_lines) == 2:
                print('File not formatted correctly')
                break
            wavelength = float(split_lines[0])
            flux = float(split_lines[1])
            data_tuple = (wavelength, flux)
            ret_val.append(data_tuple)
        return ret_val
    except FileNotFoundError:
        return None


def segment_file(spectrum, min_wavelength, max_wavelength):
    segmented_spectrum = list()
    for s in spectrum:
        if (s[WAVELENGTH_TUPLE_INDEX] >= min_wavelength) and (s[WAVELENGTH_TUPLE_INDEX] < max_wavelength + 1):
            segmented_spectrum.append(s)
    return segmented_spectrum


def get_directory(min_lambda, max_lambda, indefinite_mode, range_spectrum=None, overlap=None):
    minimum = int(min_lambda)
    maximum = int(max_lambda)
    #  make an output folder if it doesn't already exist
    output_path = os.getcwd() + "\\output\\"
    os.makedirs(output_path, exist_ok=True)
    directory_name = output_path
    if not indefinite_mode:
        #  make a specific folder for the splitting if it is in definite mode
        directory_name = output_path + "\\%s_%s_%s_%s\\" % (minimum, maximum, range_spectrum, overlap)
        os.makedirs(directory_name, exist_ok=True)
    return directory_name


def make_file_indefinitely(directory, segment, min_lambda, max_lambda):
    minimum = int(min_lambda)
    maximum = int(max_lambda)
    try:
        file_name = os.path.join(directory, "%s_%s.txt" % (minimum, maximum))
        output = open(file_name, "w")
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


def make_file_definite(directory, segment, min_lambda, max_lambda):
    minimum = int(min_lambda)
    maximum = int(max_lambda)
    try:
        file_name = os.path.join(directory, "%s_%s.txt" % (minimum, maximum))
        output = open(file_name, "w")
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
