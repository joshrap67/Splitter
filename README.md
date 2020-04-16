# Splitter
Astronomy command line program for segmenting large text files containing data of quasar spectra.

## Getting Started

One easy way of using this program is to clone this repository in its own folder and then move files needed to be segmented into it as needed.

Or, you can save the path of the main.py and create an alias to call it anywhere on your machine.

## Prerequisites

Python is required for this program to run (version 3.70 is recommended).

Note that this program will *NOT* work on Python2.

You must have at least one .txt file that is space delimited, with two columns, in the root directory of the program. The data is expected to be floating point numbers with the first column corresponding to the wavelength of the spectrum and the second the flux. A sample data .txt file is provided in this repository.

## Deployment

To run this program, execute the following command in the root directory of this program:

`python main.py`

This program works on both Windows and Linux.

## Usage

The main usage of this program is for segmenting large text files that are used in analysis of quasars in astrophysics research. Certain programs, such as IRAF, allow you to create plots of flux vs. wavelength and in order to normalize the spectrum, you must break up the spectrum into smaller pieces and doing that requires separate text files that are segmented from the original, often large, spectrum that can range up to 20000 λ.

This program presents two main options for the user to select. Creating files from a given range or creating files individually. All output is put into a generated folder "output".

### Given Range

When choosing this option, the user must supply a minimum wavelength, maximum wavelength, range, and overlap. The minimum wavelength is the smallest wavelength that will be in the segmented files and the maximum the largest.

The range dictates the range of each segmented file. For example, if a range of 500 is given for a minimum wavelength of 1000 and maximum wavelength of 2000, then two files will be produced with the first starting at 1000 and ending at 1500, and the second starting at 1500 and ending at 2000 (assuming no overlap, covered below). Note that since the numbers are floating point, the first file would include a value such as 1500.6490.

The overlap dictates how many points overlap into subsequent generated segmented files. For example, if an overlap of 50 was given in the previous example, then the second file would start at 1450 instead of 1500.

The files are placed into a folder inside the output directory with the following schema:

minimumWavelength_maximumWavelength_range_overlap

Do note that if you run the program again with the exact same parameters, it will overwrite the old folder. The files within this folder have the following schema:

minimumWavelengthOfFile_maximumWavelengthOfFile

### Individually

When choosing this option, the user must supply a minimum wavelength and a maximum wavelength. Single files can be made over and over until the user types in a specific key word to exit this mode. Files are placed directly into the output directory.

The files have the following schema:

minimumWavelengthOfFile_maximumWavelengthOfFile

## Built With

- [Python](https://www.python.org/)

## Authors

- Joshua Rapoport - *Creator and Main Software Developer*
