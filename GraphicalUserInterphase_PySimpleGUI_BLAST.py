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
imageBioPython_path = os.path.join(script_dir, "./Brand/Biopython_logo.png")
size = (120,80)
im = Image.open(imageBioPython_path)
im = im.resize(size, resample=Image.BICUBIC)

imageANSO_path = os.path.join(script_dir, "./Brand/ANSO.png")
size = (260,206)
im2 = Image.open(imageANSO_path)
im2 = im2.resize(size, resample=Image.BICUBIC)

imageNCBI_BLAST_path = os.path.join(script_dir, "./Brand/NCBI_BLAST.png")
size = (50,71)
im3 = Image.open(imageNCBI_BLAST_path)
im3 = im3.resize(size, resample=Image.BICUBIC)

imageClustalOmega_path = os.path.join(script_dir, "./Brand/ClustalOmega.png")
size = (100,100)
im4 = Image.open(imageClustalOmega_path)
im4 = im4.resize(size, resample=Image.BICUBIC)

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





# Create the layouts -------------------------------------------------------------
# Define the layout of the introduction tab 
intro_layout_column = [[sg.Text('Welcome to ANSO', font='AnyFont 25 bold', size=(105,None), justification=CENTER)],
                       [sg.Image(size=(260,206), key='-IMAGE2-', pad=(10,10))],
                       [sg.Text('Alignment Navigated Sequence Organizer', font='AnyFont 20')],
                       [sg.Text("This application is a versatile bioinformatics tool designed to streamline sequence analysis tasks.\
With ANSO, you have the flexibility to perform various essential functions such as BLAST, Multiple \
Sequence Alignment (MSA), and visualization of phylogenetic trees based on neighborhood analysis. \
Whether you need to quickly search for similar sequences, align multiple sequences for comparizon, \
or explore the evolutionary relationships among sequences, ANSO provides a user-friendly interfase \
to carry out these tasks efficiently. The modular design of ANSO allows you to utilize each tool \
independently or seamlessly integrated them together, enabling a seamless and comprehensive sequence \
analysis workflow.", font='AnyFont 9', size=(103, None), justification='center')],
                       [sg.Image(size=(120,80), key='-IMAGE-', pad=(10,10))],
                       [sg.Button('Get started', font='AnyFont 16 bold', key='-GET_STARTED-')]]
intro_layout = [[sg.Column(intro_layout_column, element_justification='center')]]

# Define the layout of the blast tab
blast_layout = [[sg.Text('Basic Local Alignment Search Tool (BLAST)', font='AnyFont 18'),
                 sg.Image(size=(100,142), key='-IMAGE3-')],
                [sg.Text('BLAST is a widely used bioinformatics algorithm and software tool for \
sequence similarity searching. It is performed to compare a query sequence against a database of \
known sequences to identify similar sequences and infer functional or evolutionary relationships.\
\n\nThe main purpose of performing a BLAST search is to determine the similarity between a query \
sequence and sequences in a database. BLAST uses an algorithm that rapidly aligns the query \
sequence with sequences in the database and calculates a similarity score. This score indicates \
the degree of sequence similarity or homology between the query and database sequences.',
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
                sg.FileBrowse(key='-BROWSE-'),
                sg.Input(enable_events=True, key='-INFILE-', border_width=0, background_color='#9FB8AD',
                         font='Anyfont 12 bold')],
                
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

                [sg.Button('BLAST')],
                [sg.Text('\n')],
                [sg.Button('< Back'), sg.Text('\t\t\t\t\t\t\t\t\t\t     '), sg.Button('Next >')]
                ]

# Define the layout of the MSA tab
msa_layout = [[sg.Text('Multiple Sequence Alignment (MSA)', font='AnyFont 15'), sg.Image(size=(100,100), key='-IMAGE4-')],
              [sg.Text('The Multiple Sequence Alignment (MSA) tool in ANSO harnesses the power \
of the online Clustal Omega algorithm to perform accurate and efficient sequence alignments. By \
leveraging the Clustal Omega tool, ANSO ensures that your sequences are aligned with precision, \
considering both sequence conservation and structural compatibility.', size=(105,None))],
              [sg.Button('< Back'), sg.Text('\t\t\t\t\t\t\t\t\t\t     '), sg.Button('Next >')]]

# Define the layout of the MSA tab
tree_layout = [[sg.Text('This is the Tree layout')],
               [sg.Button('< Back')]]

# Define the layout of the log tab
log_layout = [[sg.Multiline(size=(100,10), font='Courier 8',
                            write_only=True,
                            reroute_stdout=True, reroute_stderr=True,
                            echo_stdout_stderr=True, autoscroll=True,
                            auto_refresh=True)],
              [sg.Button('Exit')]]
                            
# Create the main layout -----------------------------------------------------
layout = [[sg.MenubarCustom(menu_def, key='-MENU-',
                            font='Courier 15', tearoff=True)],
          [sg.Text('BLAST',
                   justification='center', font='AnyFont 20 bold',
                   relief=sg.RELIEF_RAISED,
                   enable_events=True, expand_x=True)],

          [sg.Column(
                [[sg.TabGroup(
                    [[sg.Tab('Start', intro_layout, key='-START_TAB-'),
                      sg.Tab('BLAST', blast_layout, key='-BLAST_TAB-'),
                      sg.Tab('MSA', msa_layout, key='-MSA_TAB-'),
                      sg.Tab('Tree', tree_layout, key='-TREE_TAB-')]],
                      size=(750,800), expand_y=True, key='-TABGROUP-'
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

# Create the window ----------------------------------------------------------
window = sg.Window('Graphical User Interphase', layout,
                   grab_anywhere=True,
                   size=(1400,800), use_custom_titlebar=True,
                   finalize=True, keep_on_top=True)
    
# Convert im to ImageTK.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im)
image2 = ImageTk.PhotoImage(image=im2)
image3 = ImageTk.PhotoImage(image=im3)
image4 = ImageTk.PhotoImage(image=im4)

window['-IMAGE-'].update(data=image)
window['-IMAGE2-'].update(data=image2)
window['-IMAGE3-'].update(data=image3)
window['-IMAGE4-'].update(data=image4)

##############################################################################
##############################################################################
#                                Event loop                                  #
##############################################################################
##############################################################################
# switching between the tabs with "< Back", and "Next >"
countingtab = 1
taborder = ['-START_TAB', '-BLAST_TAB-', '-MSA_TAB-', '-TREE_TAB-']
                             
# Event loop -----------------------------------------------------------------
while True:
    event, values = window.read(timeout=100)

    # Log every interaction with the Graphical User Interphase
    if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
        print('=========== Event = ', event, ' ============ ')
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
    
    if event == "-GET_STARTED-":
        print("[LOG] Get started")
        window['-BLAST_TAB-'].select()
        countingtab =+ 1
    
    if event == "< Back":
        print("[LOG] Went to previous tab")
        countingtab =- 1


    if event == "Next >":
        print("[LOG] Went to the next tab")
        countingtab =+ 1


    if event == "-BROWSE-":
        print("[LOG] Browsed after file")
        selected_file = values['-BROWSE-']
        window['-INFILE-'].update(selected_file)
    
    if event == "BLAST":
        print("[LOG] Clicked 'BLAST'")
        # Ask for input --------------------------------------------------------------
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import TimeoutException
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

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
        print('Blast has started')

        max_wait_time = 80
        update_interval = 5

        wait = WebDriverWait(driver, update_interval)

        try:
            driver.find_element(By.ID, "type-a")
            wait.until(EC.staleness_of(driver.find_element(By.ID, "type-a")))
        except:
            print('The server access is minimal, try again later...')
            pass

        while max_wait_time > 0:
            try:
                download_button = wait.until(EC.element_to_be_clickable((By.ID, "btnDwnld")))
                download_button.click()
                print("clicked download button")
                download_button2 = driver.find_element(By.ID, 'dwFST')
                download_button2.click()
                break
            except TimeoutException:
                max_wait_time -= update_interval
                continue
            
window.close()