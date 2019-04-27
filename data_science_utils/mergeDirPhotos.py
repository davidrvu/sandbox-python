# DAVIDRVU - 2019

# pip install exifread

from PIL import Image
from printDeb import printDeb
import exifread
import os
import shutil
import sys

def get_date_taken(path):
    try:
        return Image.open(path)._getexif()[36867]
    except Exception:
        #with open(path, 'rb') as fh:
        #    tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
        #    dateTaken = tags["EXIF DateTimeOriginal"]
        #    return dateTaken

        with open(path, "rb") as img: # Change "11.jpg" to filename variable
            exif = exifread.process_file(img)

            print("exif = ")
            print(exif)

            print("path = " + str(path)) # TODOTODO!!!!

            print(Image.open(path)._getexif())
            sys.exit()
            if "DateTimeOriginal" in exif:
                dt = str(exif["EXIF DateTimeOriginal"])
                # into date and time
                #ay, dtime = dt.split(" ", 1)
                #hour, minute, second = dtime.split(":", 2)
                print("dt = " + str(dt))
                return dt
            else:
                print("asdasdasd")

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

    if len(folders_list) == 0:
        folders_list = [""]

    print("MAIN LOOP ! ")
    for curr_folder in folders_list:
        print("curr_folder = " + str(curr_folder))
        photos_list = next(os.walk(photo_dir+"/"+curr_folder))[2]
        print("photos_list = ")
        print(photos_list)
        for curr_photo in photos_list:
            if curr_folder == "":
                curr_filename = photo_dir+"/"+curr_photo
            else:
                curr_filename = photo_dir+"/"+curr_folder+"/"+curr_photo
            print("    curr_filename = " + str(curr_filename))
            date_taken = getDatetime_capture(debug, curr_filename)
            if curr_folder == "":
                out_filename = merge_dir+"/"+date_taken+"_"+curr_photo
            else:
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
    #photo_dir = "E:/merge_photos"
    #merge_dir = "E:/merge_photos/merged"

    photo_dir = "E:/fotos_yosemite/celular_alfredo"
    merge_dir = "E:/fotos_yosemite/celular_alfredo_fecha"
    ##########################################################################################

    mergeDirPhotos(debug, photo_dir, merge_dir)

    print("DONE!")

if __name__ == "__main__":
    main()