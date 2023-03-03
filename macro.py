# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:35:13 2022

@author: Ehlion
"""

import os
import zipfile
import re

WDIR="E:\\_Anthology\\Icerya Eiyuusenki"
extension=".png"
nbr_digit_target=3
target_pattern = re.compile(f"([0-9]{{{nbr_digit_target}}}).(.*)")

os.chdir(WDIR)

print(os.getcwd())

for file in os.listdir() :

    # check is a zip file
    if zipfile.is_zipfile(file) :
        print("start ",file)
        zf = zipfile.ZipFile(file)

        command_rename_arguments=""

        # for every file in the archive
        for zipinfo in zf.infolist() :
            match = target_pattern.match(zipinfo.filename)
            fname = zipinfo.filename.split('.')[0]

            # if not the correct number of digits
            if not match :
                # Check is a number and len<target
                if not int(fname) :
                    print("Ignored (NaN) : " + zipinfo.filename)
                elif len(fname)>nbr_digit_target :
                    print("Ignored (too long) : " + zipinfo.filename)
                else :
                    # count missing digits
                    add_zero = nbr_digit_target - len(fname)
                    # get new name
                    new_name = "0"*add_zero + zipinfo.filename

                    # add to the rename arguments
                    command_rename_arguments += f" \"{zipinfo.filename}\" \"{new_name}\""
        zf.close()

        # call the 7z system command
        # if some files to rename
        if len(command_rename_arguments) > 0 :
            print("Rename files in : ", file)

            # print(f"7z rn \"{file}\" \"{zipinfo.filename}\" \"{new_name}\"")
            command = f"7z rn \"{file}\"" + command_rename_arguments
            check = os.system(command)

            if check == 0 :
                pass #no error to report
            elif check == 1 :
                print(" : Warning (Non fatal error(s)). For example, one or more files were locked by some other application, so they were not compressed.")
            elif check == 2 :
                print("Fatal error")
            elif check == 7 :
                print("Command line error")
            elif check == 8 :
                print("Not enough memory for operation")
            elif check == 255 :
                print("User stopped the process")
            else :
                print("Unknown error code !!")
            if check != 0 :
                print("command was ", command)

# resize pictures
from PIL import Image
import os

WDIR="E:\\suukaizou\\[suukaizou] Xuanzang training [Eng]"

os.chdir(WDIR)

print(os.getcwd())

for file in os.listdir() :
    print(file)
    image = Image.open(file)
    print(image.size)
    image.thumbnail((1280, 1804))
    print(image.size)
    image.save(file)
    image.close()