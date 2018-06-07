# Written by Joshua Rapoport


class Quasar(object):
    wavelength_quasar = 0
    flux_quasar = 0

    def __init__(self, a_wavelength, a_flux):
        self.set_wavelength(a_wavelength)
        self.set_flux(a_flux)

    def set_wavelength(self, a_wavelength):
        self.wavelength_quasar = a_wavelength

    def set_flux(self, a_flux):
        self.flux_quasar = a_flux

    def get_wavelength(self):
        return self.wavelength_quasar

    def get_flux(self):
        return self.flux_quasar

    @classmethod
    def read_file(cls, file_name):
        if file_name is None:
            return None
        try:
            read_segment = list()
            working_file = open(file_name, 'r')
            for line in working_file:
                line = line.rstrip()
                split_lines = line.split()
                if not len(split_lines) == 2:
                    print('File not formatted correctly')
                    break
                a_wavelength = float(split_lines[0])
                a_flux = float(split_lines[1])
                a_point = Quasar(a_wavelength, a_flux)
                read_segment.append(a_point)
            return read_segment
        except FileNotFoundError:
            return None

    @classmethod
    def segment(cls, spectrum, min_lambda, max_lambda):
        segmented_spectrum = list()
        for s in spectrum:
            if (s.get_wavelength() >= min_lambda) and (s.get_wavelength() < max_lambda+1):
                segmented_spectrum.append(s)
        return segmented_spectrum

    @classmethod
    def make_file(cls, segment, min_lambda, max_lambda):
        minimum = int(min_lambda)
        maximum = int(max_lambda)
        try:
            output = open("%s_%s.txt" % (minimum, maximum), "w")
            for j in range(0, len(segment)-1, 1):
                if j is None:
                    break
                unformatted_wavelength = segment[j].get_wavelength()
                unformatted_flux = segment[j].get_flux()
                formatted_wavelength = "{0:.6f}".format(unformatted_wavelength)  # 6 digits after decimal point
                formatted_flux = "{0:.6f}".format(unformatted_flux)  # 6 digits after decimal point
                output.write("%s %s\n" % (formatted_wavelength, formatted_flux))
            # to prevent the last line of the file from being blank.
            unformatted_wavelength = segment[len(segment)-1].get_wavelength()
            unformatted_flux = segment[len(segment)-1].get_flux()
            formatted_wavelength = "{0:.6f}".format(unformatted_wavelength)
            formatted_flux = "{0:.6f}".format(unformatted_flux)
            output.write("%s %s" % (formatted_wavelength, formatted_flux))
            output.close()
        except FileNotFoundError:
            print("Error")

    @classmethod
    def sort_values(cls, unsorted_list):
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for value in range(0, len(unsorted_list)-1, 1):
                if unsorted_list[value].get_wavelength() > unsorted_list[value+1].get_wavelength():
                    temp = unsorted_list[value]
                    unsorted_list[value] = unsorted_list[value+1]
                    unsorted_list[value+1] = temp
                    has_swapped = True

# front end


print('Note that this program expects a text file with two columns, the space character as a delimeter,'
      '\nand the first column corresponding to wavelength and the second to flux.\n')
inputFile = input("Enter the file name (.txt extension not required) ")+".txt"
try:
    workingFile = open(inputFile, 'r')
except FileNotFoundError:
    print("File not found!")
    quit()
working_spectrum = Quasar.read_file(inputFile)
# in case the file is not sorted correctly
Quasar.sort_values(working_spectrum)
keep_using = True
while keep_using:
    decision = input("Enter:\n"
                     "\"d\" to create a definite number of files from a set range\n"
                     "\"i\" to create files indefinitely\n"
                     "\"quit\" to exit the program ")
    if decision == "d":
        min_wavelength = input("Enter the minimum wavelength: ")
        min_wavelength = float(min_wavelength)
        if min_wavelength < working_spectrum[0].get_wavelength():
            min_wavelength = working_spectrum[0].get_wavelength()  # sets min to lowest wavelength in spectrum
        max_wavelength = input("Enter the maximum wavelength: ")
        max_wavelength = float(max_wavelength)
        if max_wavelength > working_spectrum[len(working_spectrum) - 1].get_wavelength():
            max_wavelength = working_spectrum[len(working_spectrum) - 1].get_wavelength()  # sets max to largest wavelength in spectrum
        elif max_wavelength < working_spectrum[0].get_wavelength():
            print("Maximum must be in the range of the spectrum!")
            break
        elif max_wavelength == min_wavelength:
            print("Maximum cannot equal the minimum!")
            break
        elif max_wavelength < min_wavelength:
            print("Maximum must be greater than the minimum wavelength!")
            break
        range_s = input("Enter the range of the spectrum: ")
        range_s = float(range_s)
        overlap = input("Enter the overlap of the files: ")
        overlap = float(overlap)
        # determining the number of files necessary
        files_float = ((max_wavelength - min_wavelength) / range_s) * (1 + overlap / range_s)
        files = 0
        if int(files_float) == files_float:
            files = int(files_float)
        else:
            files = int(files_float) + 1
        print('Creating', files, 'files...')
        original_max = max_wavelength
        for i in range(0, files, 1):
            max_wavelength = min_wavelength + range_s
            if max_wavelength > original_max:
                # prevents overlap from altering the inputted max wavelength
                working_segment = Quasar.segment(working_spectrum, min_wavelength, original_max)
                Quasar.make_file(working_segment, min_wavelength, original_max)
            else:
                working_segment = Quasar.segment(working_spectrum, min_wavelength, max_wavelength)
                Quasar.make_file(working_segment, min_wavelength, max_wavelength)
            min_wavelength = max_wavelength - overlap
        print('Successfully created', files, 'files!')
    elif decision == "i":
        keep_adding = True
        while keep_adding:
            min_wavelength = input("Enter the minimum wavelength or \"back\" to go back to the option menu: ")
            if min_wavelength == "back":
                break
            min_wavelength = float(min_wavelength)
            if min_wavelength < working_spectrum[0].get_wavelength():
                min_wavelength = working_spectrum[0].get_wavelength()
            max_wavelength = input("Enter the maximum wavelength: ")
            max_wavelength = float(max_wavelength)
            if max_wavelength > working_spectrum[len(working_spectrum) - 1].get_wavelength():
                max_wavelength = working_spectrum[len(working_spectrum) - 1].get_wavelength()
            elif max_wavelength < working_spectrum[0].get_wavelength():
                print("Maximum must be in the range of the spectrum!")
                break
            elif max_wavelength == min_wavelength:
                print("Maximum cannot equal the minimum!")
                break
            elif max_wavelength < min_wavelength:
                print("Maximum must be greater than the minimum wavelength!")
                break
            working_segment = Quasar.segment(working_spectrum, min_wavelength, max_wavelength)
            Quasar.make_file(working_segment, min_wavelength, max_wavelength)
    elif decision == "quit":
        print("Goodbye!")
        keep_using = False
    else:
        print("Invalid Action!")
quit()
