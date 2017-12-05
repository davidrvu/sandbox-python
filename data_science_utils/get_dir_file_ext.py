import os
import sys

def get_dir_file_ext(full_path_in):
    # Se verifica que exista el archivo
    if os.path.exists(full_path_in):
        print("El archivo " + full_path_in + " SI existe")
    else:
        print("ERROR: El archivo " + full_path_in + " NO EXISTE")
        sys.exit()

    # Se separa el fullpath
    directory                     = os.path.dirname(full_path_in)
    filename_full                 = os.path.basename(full_path_in)
    filename_base, file_extension = os.path.splitext(filename_full)

    return [directory, filename_base, file_extension]