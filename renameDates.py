#! python3
# renames files in cwd by converting american date MM-DD-YYYY into EU style DD-MM-YYYY

from calendar import month
import os
import re
import sys
import shutil
dateFormat = ''
while dateFormat.lower() not in ['eu', 'us']:
    dateFormat = input('''This program converts dates in curent working directory\'s files from EU to US format and other way round.
Enter "us" to convert eu dates to us dates, enter "eu" to convert US dates to EU dates:\n''')

# compile regexex
usDatePattern = re.compile(r'''^(.*?)       # all chars before date
                            ((0|1)?\d)-         # 1/2 digits for month -
                            ((0|1|2|3)?\d)-     # 1/2 digits for day-
                            ((19|20)?\d{2})     # 2/4 digits for year
                            (.*?)$              # all cahrs after name
                            ''', re.VERBOSE)
euDatePattern = re.compile(r'''^(.*?)       # all chars before date
                            ((0|1|2|3)?\d)-     # 1/2 digits for day -
                            ((0|1)?\d)-         # 1/2 digits for month-
                            ((19|20)?\d{2})     # 2/4 digits for year
                            (.*?)$              # all cahrs after name
                            ''', re.VERBOSE)

if dateFormat == 'eu':
        # loop through cwd files list
    for file in os.listdir(os.getcwd()):
        # assign return value of regex search
        mo = usDatePattern.search(file)
        # to avoid mutilating eu date patterns already in directory
        euCheck = euDatePattern.search(file)
        # skip non-dates
        if mo == None or euCheck != None:
            continue
        # assign found groups to variables
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
        # combine new filename
        euName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
        # get absolute paths for renaming
        absCWD = os.path.abspath('.')
        usFilename = os.path.join(absCWD, file)
        euFilename = os.path.join(absCWD, euName)
        # rename file, uncommebt last line if needed
        print(f'Renaming {usFilename} to {euFilename}.')
        # shutil.move(usFilename, euFilename) 

elif dateFormat == 'us':
    # loop through cwd files list
    for file in os.listdir(os.getcwd()):
        # assign return value of regex search
        mo = euDatePattern.search(file)
        # skip non-dates
        if mo == None:
            continue
        # assign found groups to variables
        beforePart = mo.group(1)
        dayPart = mo.group(2)
        monthPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
        # combine new filename
        usName = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart
        # get absolute paths for renaming
        absCWD = os.path.abspath('.')
        euFilename = os.path.join(absCWD, file)
        usFilename = os.path.join(absCWD, usName)
        # rename file, uncommebt last line if needed
        print(f'Renaming {euFilename} to {usFilename}.')
        # shutil.move(usFilename, euFilename) 