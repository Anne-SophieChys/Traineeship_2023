#!/usr/bin/python3
##############################################################################
##############################################################################
#                           Graphical User Interphase                        #
##############################################################################
##############################################################################

# Installations ##############################################################
# pip install pysimplegui (v4.60.4)
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

#=============================================================================
#========================= BLAST Settings ====================================
#=============================================================================
# BLAST Settings
from bs4 import BeautifulSoup
import urllib
import urllib.request
import sys

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
url = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

except Exception as e:
    sys.exit("{}\nSearching blast.ncbi.nlm.nih.gov/Blast.cgi --> Q5QLK3\n", e)

soup = BeautifulSoup(data, "html.parser")
#=============================================================================
#=============================================================================
#=============================================================================


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
size=(105,None), expand_x=True)],
                [sg.Text('Program Selection', font='AnyFont 12 bold')],
                [sg.Combo(values=('blastn', 'blastp', 'blastx', 'tblastn', 'tblastx'),
                          default_value='blastn',
                          readonly=True,
                          key='-BLASTTYPE-')],

                [sg.Text('Enter Query Sequence', font='AnyFont 12 bold')],
                [sg.Text('Enter accession number(s) or FASTA sequence(s)', font='AnyFont 9 bold')],
                [sg.Multiline(key= '-QUERY-', size=(111,6)), sg.InputText()],

                [sg.Text('Or, upload file', font='AnyFont 9 bold'),
                sg.VSeparator(),
                sg.FileBrowse(),
                sg.Input(key='-INFILE-', border_width=0, background_color='#9FB8AD')],
                
                [sg.Text('Job Title\t          ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Input(key='-JOBTITLE-', border_width=0)],

                [sg.Text('Database          ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Combo(values=('Reference RNA sequence (refseq_rna)',
                                  'RefSeq Genome Database (refseq_genomes)',
                                  'PDB nucleotide database (pdb)',
                                  'Non-redundant protein sequences (nr)',
                                  'UniProtKB/Swiss-Prot(swissprot)',
                                  'Patented protein sequences(pataa)',
                                  'Metagenomic proteins(env_nr)',
                                  'Transcriptome Shotgun Assembly proteins (tsa_nr)'),
                         key='-DB-')],
                
                [sg.Text('Algorithm parameters', font='AnyFont 12 bold')],
                [sg.Text('Max target \nsequences        ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Combo(values=(10,50,100,200,250,500,1000,5000),
                          default_value='100',
                          key='-MAXTS-')],

                [sg.Text('Threshold         ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Input(key='-THRESHOLD-', size=(5,0), default_text=0.05)],

                [sg.Button('BLAST')]
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
                      size=(750,800), expand_y=True
                )]], sbar_relief=sg.RELIEF_RAISED),

          sg.Column(
                    [[sg.Frame('', log_layout, border_width=0,
                               pad=((0,0),(20,0)))]],
                               expand_y=True)
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
                   finalize=True, keep_on_top=True)
    
# Convert im to ImageTK.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im)
window['-IMAGE-'].update(data=image)

# Event loop -------------------------------------------------------------
while True:
    event, values = window.read(timeout=100)

    # Log
    if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
        print('=========== Event = ', event, ' ============ ')
        print('----- Values Directory (key=value) -----')
        for key in values:
            print(key, ' = ', values[key])

    if event in (None, 'Exit'):
        print("[LOG] Clicked on 'Exit'")

        # Ask for input --------------------------------------------------------------
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        program = values['-BLASTTYPE-']
        location = url + "?PROGRAM=" + program + "&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome"

        driver = webdriver.Firefox()
        driver.get(location)

        # Get information about the -QUERY-
        inputquery = values['-QUERY-']
        # inputfile = values['--'] browse doesn't work yet
        query = driver.find_element(By.ID, "seq")
        query.send_keys(inputquery)

        # Get information about the -JOBTITLE-
        inputjobtitle = values['-JOBTITLE-']
        jobtitle = driver.find_element(By.NAME, "JOB_TITLE")
        jobtitle.send_keys(inputjobtitle)

        # Get information about the -DB-
        inputdatabase = values['-DB-']
        database = driver.find_element(By.NAME, "DATABASE")
        database.send_keys(inputdatabase)

        # # Click on the BLAST Button
        # Algorithmbutton = driver.find_element(By.CLASS_NAME, "usa-accordion-button")
        # Algorithmbutton.click()

        # # Get information about the -MAXTS-
        # inputmax = values['-MAXTS-']
        # max = driver.find_element(By.NAME, "MAX_NUM_SEQ")
        # max.send_keys(inputmax)

        # # Get information about the -THRESHOLD-
        # inputthreshold = values['-THRESHOLD-']
        # threshold = driver.find_element(By.NAME, "EXPECT")
        # threshold.send_keys(inputthreshold)

        # Click on the BLAST Button
        blast = driver.find_element(By.CLASS_NAME, "blastbutton")
        blast.click()


        break

    if event == 'About':
        print("[LOG] Clicked on 'About'")
        sg.popup('This is what happens when you \'click\' on About',
                    'Programming Luanguage :: Python v3.10.10',
                    'Application :: PySimpleGUI v4.60.4',
                    'url :: \"https://github.com/PySimpleGUI/PySimpleGUI\"',
                    keep_on_top=True)
            
    # if event == "Browse":
    #     print("[LOG] Clicked 'Browse'")
    #     selected_file = values['-BROWSEFILE-']
    #     if selected_file:
    #         file_name = selected_file.split('/')[-1]
    #         window['-BROWSEFILE-'].update(file_name)
    
    if event == "Submit":
        print("[LOG] Clicked 'Submit'")

window.close()