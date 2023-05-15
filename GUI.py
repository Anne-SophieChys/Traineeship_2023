#!/usr/bin/python3
##############################################################################
##############################################################################
#                           Graphical User Interphase                        #
##############################################################################
##############################################################################

# Installations ##############################################################
# pip install pysimplegui
# Load the packages ----------------------------------------------------------
import PySimpleGUI as sg
from PIL import Image, ImageTk
import os


# Navigations ################################################################
# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image file
image_path = os.path.join(script_dir, "Biopython_logo.png")
size = (120,80)
im = Image.open(image_path)
im = im.resize(size, resample=Image.BICUBIC)

# Developping BLAST ##########################################################







# Developping Interfase ######################################################
# Make the window theme ------------------------------------------------------
def make_window(theme):
    sg.theme(theme)
    # Define the menu
    menu_def = [['&File', ['Exit']],
                ['&Edit', ['Dark mode']],
                ['&Help', ['About']]
    ]

    # Create the layouts -----------------------------------------------------
    # Define the layout of the introduction tab 
    intro_layout = [[sg.Text('Introduction', font='AnyFont 12 bold')],
                    [sg.Text('This application can be used...')],
                    [sg.Image(size=(180,80), key='-IMAGE-', pad=(10,10))]]

    # Define the layout of the blast tab
    blast_layout = [[sg.Text('BLAST (Basic Local Alignment Search Tool) is \
a widely used bioinformatics algorithm and software tool for sequence \
similarity searching. It is performed to compare a query sequence against \
a database of known sequences to identify similar sequences and infer \
functional or evolutionary relationships.\n\nThe main purpose of performing a \
BLAST search is to determine the similarity between a query sequence and \
sequences in a database. BLAST uses an algorithm that rapidly aligns the \
query sequence with sequences in the database and calculates a similarity \
score. This score indicates the degree of sequence similarity or homology \
between the query and database sequences.',
size=(111,None), auto_size_text=True)],

                [sg.Text('Enter Query Sequence', font='AnyFont 12 bold')],
                [sg.Text('Enter accession number(s) or FASTA sequence(s)',
                         font='AnyFont 9 bold')],
                [sg.Multiline(s=(111,10))],
                [sg.Text('Or, upload file',
                         font='AnyFont 9 bold')],
                [sg.Button('Browse')]

]

    # Define the layout of the MSA tab
    msa_layout = [[sg.Text('This is the MSA layout')]]


    # Create the main layout -------------------------------------------------
    layout = [[sg.MenubarCustom(menu_def, key='-MENU-',
                                font='Courier 15', tearoff=True)],
               [sg.Text('BLAST', size=(len('Start')+3,1), justification='center',
                       font='AnyFont 20 bold', relief=sg.RELIEF_RAISED,
                       k='-TEXT HEADING-', enable_events=True,
                       expand_x=True)]]

    layout += [[sg.TabGroup([[sg.Tab('Start', intro_layout),
                              sg.Tab('BLAST', blast_layout),
                              sg.Tab('MSA', msa_layout)]],
                              key='-TAB GROUP-', expand_x=True,
                              expand_y=True)]]

    # Create the window ------------------------------------------------------
    window = sg.Window('Graphical User Interphase', layout,
                       grab_anywhere=True,
                       size=(800,800), use_custom_titlebar=True,
                       finalize=True, keep_on_top=True,)
    
    # Convert im to ImageTK.PhotoImage after window finalized
    image = ImageTk.PhotoImage(image=im)
    window['-IMAGE-'].update(data=image)
    
    return window


def main():
    # Create the window with the 'LightBrown2' theme
    window = make_window(sg.theme('LightBrown2'))

    # Event loop
    while True:
        event, values = window.read(timeout=100)

        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('========== Event = ', event, ' ========== ')
            print('----- Values Directory (key=value) -----')
            for key in values:
                print(key, ' = ', values[key])

        if event in (None, 'Exit'):
            print("[LOG] Clicked on 'Exit'")
            break

        if event == 'About':
            print("[LOG] Clicked on 'About'")
            sg.popup('This is what happens when you \'click\' on About',
                     'Programming Luanguage :: Python v3.10.10',
                     'Application :: PySimpleGUI v4.60.4',
                     'url :: \"https://github.com/PySimpleGUI/PySimpleGUI\"',
                     keep_on_top=True
                     )
        elif event == "Browse":
            print("[LOG] Clicked 'Browse'")
            folder_or_file = sg.popup_get_file('Choose your folder',
                                               keep_on_top=True),
            




    window.close()

if __name__ == '__main__':
    # Set the PySimpleGUI themse
    sg.theme('black')
    sg.theme('dark red')
    sg.theme('dark green 7')
    # sg.theme('DefaultNoMoreNagging')

    # Run the main function
    main()