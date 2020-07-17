# DAVIDRVU -2020

from PIL import Image, ImageDraw, ImageFont 
import numpy as np
import PIL.ImageOps    
import random
import sys

def getPixelValues(input_im_file, resample_size):
    print("\n----> START " + str(sys._getframe().f_code.co_name) )
    image_file_original = Image.open(input_im_file)
    im_size_original    = image_file_original.size
    image_inv           = PIL.ImageOps.invert(image_file_original)

    #image_gray = image_inv.convert('LA') # convert image to black and white
    image_gray = image_file_original.convert('LA') # convert image to black and white

    # Resize smoothly down
    imgSmall  = image_gray.resize((resample_size,resample_size), resample=Image.BILINEAR)
    #print(imgSmall.size)
    # Scale back up using NEAREST to original size
    image_out = imgSmall.resize(im_size_original, Image.NEAREST)
    pixels_matrix = np.array(imgSmall)
    return pixels_matrix

def getMatrixImage(pixels_matrix, bright_factor, font_path, font_size, char_matrix, output_size):
    print("\n----> START " + str(sys._getframe().f_code.co_name) )
    base = Image.new('RGBA', output_size, color = (0, 0, 0, 255))
    # make a blank image for the text, initialized to transparent text color
    txt_foreground = Image.new('RGBA', output_size, (255,255,255,0))

    d = ImageDraw.Draw(txt_foreground)
    fnt = ImageFont.truetype(font_path, font_size)

    for i in range(0,255): # FILAS
        for j in range(0,255): # COLUMNAS
            index_char = random.randint(0,len(char_matrix)-1)
            d.text((j*5, i*5), char_matrix[index_char], font=fnt, fill=(0, 255, 0, min(int(bright_factor*pixels_matrix[i,j,0]),255)  ))

    out = Image.alpha_composite(base, txt_foreground)
    #out.show()
    return out, txt_foreground

def addBackground(txt_foreground, pixels_matrix, bright_factor, font_path, font_size, char_matrix, output_size):
    print("\n----> START " + str(sys._getframe().f_code.co_name) )

    base = Image.new('RGBA', output_size, color = (0, 0, 0, 255))

    txt_background = Image.new('RGBA', output_size, (255,255,255,0))

    d = ImageDraw.Draw(txt_background)
    fnt = ImageFont.truetype(font_path, font_size)

    for j in range(0,255): # COLUMNAS
        col_prob = random.uniform(0, 1)
        if col_prob > 0.5:
            max_fila = random.randint(0,200)
            for i in range(0,max_fila): # FILAS
                index_char = random.randint(0,len(char_matrix)-1)
                if pixels_matrix[i,j,0]==0: # AGREGAR BACKGROUND SÓLO SI NO EXISTE FOREGROUND!
                    d.text((j*5, i*5), char_matrix[index_char], font=fnt, fill=(0, 255, 0, random.randint(0,150)))

    matrix_background = Image.alpha_composite(base, txt_background)
    #matrix_background.show()
    out_matrix_im = Image.alpha_composite(matrix_background, txt_foreground)
    #out_matrix_im.show()
    return out_matrix_im

def main():
    ##############################################################
    # PARAMETROS
    ##############################################################
    input_im_file = "C:/Users/david/Pictures/face4.jpg"
    out_im_file   = "C:/Users/david/Pictures/face4_matrix.png"
    font_path     = "C:/WINDOWS/FONTS/CONSOLA.TTF"
    font_size     = 8
    resample_size = 256
    char_matrix   = ["D","A","V","I","D"]
    bright_factor = 2.5
    output_size   = (1280,1280)
    ##############################################################

    print("======== THE MATRIX - PHOTOS ========")
    pixels_matrix = getPixelValues(input_im_file, resample_size)
    out_matrix_im, txt_foreground = getMatrixImage(pixels_matrix, bright_factor, font_path, font_size, char_matrix, output_size)
    out_matrix_im = addBackground(txt_foreground, pixels_matrix, bright_factor, font_path, font_size, char_matrix, output_size)
    out_matrix_im.save(out_im_file)

    print("DONE!")

if __name__ == "__main__":
    main()