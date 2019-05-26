# DAVIDRVU - 2019

# pip install pyfiglet
# FUENTE: https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts
# FUENTE: http://www.figlet.org/examples.html

import pyfiglet

def main():
    #################################################################
    ascii_banner = pyfiglet.figlet_format("Hello!!")
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='graffiti')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='avatar')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='acrobatic')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='basic')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='isometric1')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='big')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='slant')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
    #################################################################
    custom_fig = pyfiglet.Figlet(font='starwars')
    ascii_banner = custom_fig.renderText('Hello!!')
    print(ascii_banner)
    #################################################################
if __name__== "__main__":
    main()