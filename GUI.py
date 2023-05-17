#!/usr/bin/python3
##############################################################################
##############################################################################
#                           Graphical User Interphase                        #
##############################################################################
##############################################################################

# Installations ##############################################################
# pip install pysimplegui (v4.60.4)
# pip install cblaster (cblaster 1.3.18)


# Load the packages ----------------------------------------------------------
import PySimpleGUI as sg
from PIL import Image, ImageTk
import os


# Navigations ################################################################
# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image file
# image_path = os.path.join(script_dir, "Biopython_logo.png")
# size = (120,80)
# im = Image.open(image_path)
# im = im.resize(size, resample=Image.BICUBIC)

##################
##################
##################
import tkinter.filedialog

from tkinter.ttk import Style
from tkinter import *

sg.change_look_and_feel('GreenTan')

##############################################################################
##############################################################################
#                                def make_db                                 #
##############################################################################
##############################################################################
# Function code for building the database
def make_db():
    def select_fadb_button_cmd():
        global fndb
        fndb = tkinter.filedialog.askopenfilename()
        make_db_label.config(text="The files you selected:\n" + fndb)

    dbwindow = Tk()

    style.configure('Tmake_db_label.TLabel', anchor='center', font=('', 13))
    make_db_label = Label(dbwindow, text='You did not select any files', style='Tmake_db_label.TLabel')
    make_db_label.place(relx=0.041, rely=0.048, relwidth=0.602, relheight=0.105)

    style.configure('Tselect_file_button.TButton')
    select_file_button = Button(text='Select \n file',
                            command = select_fadb_button_cmd,
                            style='Tselect_file_button.TButton')
    select_file_button(relx=0.692, rely=0.015, relwidth=0.09, relheight=0.138)
    dbwindow.mainloop()    

##############################################################################
##############################################################################
#                             def make_window                                #
##############################################################################
##############################################################################
# Define the layout of the window
def make_window():
    make_db()

# Define the menu
menu_def = [['&File', ['Exit']],
            ['&Edit', ['Dark mode']],
            ['&Help', ['About']]]

# Create a Style object for customizing the window's appearance
style = Style()





# Create the layouts ---------------------------------------------------------
# Define the layout of the introduction tab 
intro_layout = [[sg.Text('Introduction', font='AnyFont 12 bold')],
                [sg.Text('This application can be used...')],
                [sg.Image(size=(180,80), key='-IMAGE-', pad=(10,10))]]

# Define the layout of the blast tab
blast_layout = [[sg.Text('BLAST (Basic Local Alignment Search Tool) is \
a widely used bioinformatics algorithm and software tool for sequence \
similarity searching. It is performed to compare a query sequence against \
a database of known sequences to identify similar sequences and infer \
functional or evolutionary relationships.\n\nThe main purpose of performing \
a BLAST search is to determine the similarity between a query sequence and \
sequences in a database. BLAST uses an algorithm that rapidly aligns the \
query sequence with sequences in the database and calculates a similarity \
score. This score indicates the degree of sequence similarity or homology \
between the query and database sequences.',
size=(111,None), auto_size_text=True)],

                [sg.Text('Enter Query Sequence', font='AnyFont 12 bold')],
                [sg.Text('Enter accession number(s) or FASTA sequence(s)', font='AnyFont 9 bold')],
                [sg.Multiline(key= '-QUERY-', size=(111,10)), sg.InputText()],
                [sg.Text('Or, upload file', font='AnyFont 9 bold'),
                 sg.Button('Browse')],
                [sg.Combo(values=('blastn', 'blastp', 'blastx', 'tblastn', 'tblastx'),
                          default_value='blastn',
                          readonly=False,
                          key='-BLASTTYPE-')],
                [sg.Multiline(key='-FILE-', size=(111,10))],
                [sg.Button('Submit')]
                ]

# Define the layout of the MSA tab
msa_layout = [[sg.Text('This is the MSA layout')]]

# Define the layout of the log tab
log_layout = [[sg.Multiline(size=(100,20), font='Courier 8',
                            write_only=True,
                            reroute_stdout=True, reroute_stderr=True,
                            echo_stdout_stderr=True, autoscroll=True,
                            auto_refresh=True)]]
                            
# Create the main layout -------------------------------------------------
layout = [[sg.MenubarCustom(menu_def, key='-MENU-',
                            font='Courier 15', tearoff=True)],
          [sg.Text('BLAST',
                   justification='center', font='AnyFont 20 bold',
                   relief=sg.RELIEF_RAISED, k='-TEXT HEADING-',
                   enable_events=True, expand_x=True)],

          [sg.Column(
                [[sg.TabGroup(
                    [[sg.Tab('Introduction', intro_layout),
                      sg.Tab('BLAST', blast_layout),
                      sg.Tab('MSA', msa_layout)]],
                      key='-COLUMN1-', size=(750,800), expand_y=True
                )]], sbar_relief=sg.RELIEF_RAISED),

          sg.Column(
                    [[sg.Frame('', log_layout, border_width=0,
                               pad=((0,0),(20,0)))]],
                               expand_y=True, key='-COLUMN2-')
                ]]
    
##############################################################################
##############################################################################
#                                 def main                                   #
##############################################################################
##############################################################################
# Main functions
def main():
    make_window(sg.theme('LightBrown2'))

# Create the window ------------------------------------------------------
window = sg.Window('Graphical User Interphase', layout,
                   grab_anywhere=True,
                   size=(1400,800), use_custom_titlebar=True,
                   finalize=True, keep_on_top=True,)
    
# Convert im to ImageTK.PhotoImage after window finalized
# image = ImageTk.PhotoImage(image=im)
# window['-IMAGE-'].update(data=image)

# Event loop -------------------------------------------------------------
while True:
    event, values = window.read(timeout=100)

    # Log
    if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
        print('=========== Event = ', event, ' =========== ')
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
                    keep_on_top=True)
            
    elif event == "Browse":
        print("[LOG] Clicked 'Browse'")
        folder_or_file = sg.popup_get_file('Choose your folder',
                                            keep_on_top = True)
        sg.popup('You chose: ' + str(folder_or_file), keep_on_top = True)
        print('[LOG] User chose file: ' + str(folder_or_file))

    #elif event == 'Process Bar'
        #         print("[LOG] Clicked Test Progress Bar!")
        # progress_bar = window['-PROGRESS BAR-']
        # for i in range(100):
        #     print("[LOG] Updating progress bar by 1 step ("+str(i)+")")
        #     progress_bar.update(current_count=i + 1)
        # print("[LOG] Progress bar complete!")
    
#     if event == '-BLASTTYPE-':
#         if values['-BLASTTYPE-'][0]:
#             window['-BLASTTYPE-'].update(values['-BLASTTYPE-'][:-1])

# print(values['-BLASTTYPE-'])

window.close()

if __name__ == '__main__':
    # Set the PySimpleGUI themse
    sg.theme('black')
    sg.theme('dark red')
    sg.theme('dark green 7')
    # sg.theme('DefaultNoMoreNagging')