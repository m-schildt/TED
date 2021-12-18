# Progress

The project has three components, all of which are being developed at the moment. The idea is to start small by making things work in the most simple fashion first, and then build on that by making more robust, elegant and efficient.

## Context

The TED FTP repository contains, among other directories, two directories with sets of compressed files: one by day called `daily-packages` and one by month called `monthly-packages`. We will be working with the former.

Within this directory, the files are stored by year and then by month. Within each month's subdirectory, there are files that follow the following naming convention: `date_file-number`. The dates follow a 'YYYYMMDD' format and the file numbers a 'YYYYXXX' format. In the latter, 'XXX' is the actual file number for that year the specific date has for that year. Only one file per day, if any, exists. All files are compressed tarballs, and thus have a `tar.gz` extension.

For example, the file for March 9, 2017 would have '20170309_2017XXX' as a name. The 'XXX' part cannot be determined in advance, as these numbers are assigned as files are generated. This means that if the first file of the year is for January 2, its name should be 'YYYY0102_YYYY001'. With this naming structure, and given that there is only one file per day, it is sufficient to search for that file which starts with a desired 'YYYYMMDD' to retrieve it if it exists.

Note that this naming convention only works for ranges of dates starting in 2011, which will be our test case. 

## Component 1: [`retrieve.py`](retrieve.py)

This file contains our work in progress of what should end up being a function that will allow a user to downlload a file with an arbitrary date with the format 'YYYYMMDD', if it exists. So far, the script is able to download a file with an arbitrary date that we know in advance exists.

## Component 2: `extract.py`

This file extracts the XMLs for a compressed tarball.

## Component 3: `write_csv.py`

This file creates a `csv` containing as many rows as XML files existed in the tarball and as many columns as XML fields were deemed relevant (explain).
