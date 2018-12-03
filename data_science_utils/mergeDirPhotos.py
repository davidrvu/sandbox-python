# DAVIDRVU - 2018

from PIL import Image
from printDeb import printDeb
import os
import shutil
import sys

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

def getDatetime_capture(debug, curr_filename):
    date_taken = get_date_taken(curr_filename)
    date_taken = date_taken.replace(":","_")
    date_taken = date_taken.replace(" ","_")
    return date_taken

def mergeDirPhotos(debug, photo_dir, merge_dir):
    printDeb(debug, "\n----> START " + str(sys._getframe().f_code.co_name) )

    folders_list = next(os.walk(photo_dir))[1]
    print("folders_list = ")
    print(folders_list)

    # Create output directory
    if not os.path.exists(merge_dir):
        os.makedirs(merge_dir)

    print("MAIN LOOP ! ")
    for curr_folder in folders_list:
        print("curr_folder = " + str(curr_folder))
        photos_list = next(os.walk(photo_dir+"/"+curr_folder))[2]
        #print(photos_list)
        for curr_photo in photos_list:
            curr_filename = photo_dir+"/"+curr_folder+"/"+curr_photo
            print("    curr_filename = " + str(curr_filename))
            date_taken = getDatetime_capture(debug, curr_filename)
            out_filename = merge_dir+"/"+date_taken+"_"+curr_folder+"_"+curr_photo
            print("    out_filename  = " + str(out_filename))
            shutil.copy2(curr_filename, out_filename)

    printDeb(debug, "----> END " + str(sys._getframe().f_code.co_name) + "\n")

def main():
    print("=============================================")
    print("== MAIN mergeDirPhotos                     ==")
    print("=============================================")

    ##########################################################################################
    ## PARAMETROS
    ##########################################################################################
    debug = 1
    photo_dir = "E:/merge_photos"
    merge_dir = "E:/merge_photos/merged"
    ##########################################################################################

    mergeDirPhotos(debug, photo_dir, merge_dir)

    print("DONE!")

if __name__ == "__main__":
    main()