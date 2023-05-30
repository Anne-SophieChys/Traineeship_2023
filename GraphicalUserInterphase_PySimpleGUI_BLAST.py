#!/usr/bin/python3
####################################################################################################################
####################################################################################################################
#                                            Graphical User Interphase                                             #
####################################################################################################################
####################################################################################################################

# Installations ----------------------------------------------------------------------------------------------------
# pip install pysimplegui (v4.60.4)

# Load the packages ------------------------------------------------------------------------------------------------
import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence
import os
import time

# Navigations ------------------------------------------------------------------------------------------------------
# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image file
imageBioPython_path = os.path.join(script_dir, "./Brand/Biopython_logo.png")
size = (180,120)
im = Image.open(imageBioPython_path)
im = im.resize(size, resample=Image.BICUBIC)

imageANSO_path = os.path.join(script_dir, "./Brand/AlignmentNavigatedSearchOrganizer.png")
size = (415,225)
im2 = Image.open(imageANSO_path)
im2 = im2.resize(size, resample=Image.BICUBIC)

imageNCBI_BLAST_path = os.path.join(script_dir, "./Brand/NCBI_BLAST.png")
size = (71,100)
im3 = Image.open(imageNCBI_BLAST_path)
im3 = im3.resize(size, resample=Image.BICUBIC)

imageClustalOmega_path = os.path.join(script_dir, "./Brand/ClustalOmega.png")
size = (100,100)
im4 = Image.open(imageClustalOmega_path)
im4 = im4.resize(size, resample=Image.BICUBIC)

#===================================================================================================================
#================================================ BLAST Settings ===================================================
#===================================================================================================================
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
    sys.exit("{}\nSearching blast.ncbi.nlm.nih.gov/Blast.cgi\n", e)

soup = BeautifulSoup(data, "html.parser")

#===================================================================================================================
#================================================ MSA Settings =====================================================
#===================================================================================================================
# MSA Settings
headersclustal = {}
headersclustal["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
urlclustal = "https://www.ebi.ac.uk/Tools/msa/clustalo/"

try:
    requestclustal = urllib.request.Request(urlclustal, headers = headersclustal)
    responseclustal = urllib.request.urlopen(requestclustal)
    dataclustal = responseclustal.read().decode("utf-8")

except Exception as e:
    sys.exit("{}\nSearching genome.jp/tools-bin/clustalw\n", e)

soup = BeautifulSoup(dataclustal, "html.parser")

#===================================================================================================================
#================================================= def make_db =====================================================
#===================================================================================================================
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

#===================================================================================================================
#============================================= def make_window =====================================================
#===================================================================================================================
# Define the layout of the window
sg.change_look_and_feel('GreenTan')

def make_window():
    make_db()

# Define the menu
menu_def = [['&File', ['Exit']],
            ['&Edit', ['Dark mode']],
            ['&Help', ['About']]]

# Create a Style object for customizing the window's appearance
import tkinter.filedialog
from tkinter.ttk import Style
from tkinter import *
style = Style()

# Create the layouts -----------------------------------------------------------------------------------------------
#===================================================================================================================
# DEFINE THE LAYOUT OF THE INTRODUCTIon TAB ========================================================================
#===================================================================================================================
intro_layout_column = [[sg.Text('Welcome to ANSO', font='AnyFont 25 bold', size=(105,None), justification=CENTER)],
                       [sg.Image(size=(260,206), key='-IMAGE2-', pad=(10,10))],
                       [sg.Text('Alignment Navigated Sequence Organizer', font='AnyFont 20')],
                       [sg.Text("This application is a versatile bioinformatics tool designed to \
streamline sequence analysis tasks. With ANSO, you have the flexibility to perform various essential \
functions such as BLAST, Multiple Sequence Alignment (MSA), and visualization of phylogenetic trees \
based on neighborhood analysis. Whether you need to quickly search for similar sequences, align \
multiple sequences for comparizon, or explore the evolutionary relationships among sequences, ANSO \
provides a user-friendly interfase to carry out these tasks efficiently. The modular design of ANSO \
allows you to utilize each tool independently or seamlessly integrated them together, enabling a \
seamless and comprehensive sequence analysis workflow.",
font='AnyFont 9', size=(103, None), justification='center')],

                       [sg.Image(size=(120,80), key='-IMAGE-', pad=(10,10))],
                       [sg.Button('Get started', font='AnyFont 24 bold', key='-GET_STARTED-')]]
intro_layout = [[sg.Column(intro_layout_column, element_justification='center', pad=(0,40))]]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE BLAST TAB ===============================================================================
#===================================================================================================================
blast_layout = [[sg.Image(size=(100,142), key='-IMAGE3-'),
                 sg.VSeparator(),
                 sg.Text('       Basic Local Alignment Search Tool (BLAST)', font='AnyFont 18')
                 ],
                [sg.Text('BLAST is a widely used bioinformatics algorithm and software tool for \
sequence similarity searching. It is performed to compare a query sequence against a database of \
known sequences to identify similar sequences and infer functional or evolutionary relationships.\
\n\nThe main purpose of performing a BLAST search is to determine the similarity between a query \
sequence and sequences in a database. BLAST uses an algorithm that rapidly aligns the query \
sequence with sequences in the database and calculates a similarity score. This score indicates \
the degree of sequence similarity or homology between the query and database sequences.',
size=(105,None), expand_x=True)],
                [sg.Text('Select the program settings: '),
                sg.Combo(values=('blastn', 'blastp', 'blastx', 'tblastn', 'tblastx'),
                          default_value='blastn',
                          readonly=True,
                          key='-BLASTTYPE-')],

                [sg.Text('Enter Query Sequence', font='AnyFont 12 bold')],
                [sg.Text('Enter accession number(s) or FASTA sequence(s)', font='AnyFont 9 bold')],
                [sg.Multiline(key= '-QUERY-', size=(111,6))],

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

                [sg.Text('\t\t\t\t\t       '),
                 sg.Button('BLAST', font='AnyFont, 13')],
                [sg.Text('\t\t\t\t\t          '),
                 sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, key='-GIF1-',
                          enable_events=True, visible=True)],

                [sg.Button('< Back', font='AnyFont, 10', key='-B1-'),
                 sg.Text('\t\t\t\t\t\t\t\t\t\t     '),
                 sg.Button('Next >', font='AnyFont, 10', key='-N1-')]
                ]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE MSA TAB =================================================================================
#===================================================================================================================
msa_layout = [[sg.Image(size=(100,100), key='-IMAGE4-'),
               sg.VSeparator(),
               sg.Text('       Multiple Sequence Alignment (MSA)', font='AnyFont 18')],
              [sg.Text('The Multiple Sequence Alignment (MSA) tool in ANSO harnesses the power \
of the online Clustal Omega algorithm to perform accurate and efficient sequence alignments. By \
leveraging the Clustal Omega tool, ANSO ensures that your sequences are aligned with precision, \
considering both sequence conservation and structural compatibility.', size=(105,None))],

              [sg.Text('Type of sequence: '), 
               sg.Combo(values=('PROTEIN', 'DNA', 'RNA'), key='-TYPE2SEQ-', default_value='PROTEIN',
                        size=(9,0), enable_events=True)],
              [sg.Text('Enter Query Sequences', font='AnyFont 12 bold')],
              [sg.Text('Support Formats: FASTA, GCG, EMBL (Nucleotide only), GenBank, PIR/NBRF, PHILIP or UniProtKB/Swiss-Prot (Protein only)', font='AnyFont 9 bold')],
              [sg.Multiline(key= '-QUERYMSA-', size=(111,6))],
              [sg.Text('Or, upload file', font='AnyFont 9 bold'),
               sg.VSeparator(),
               sg.FileBrowse(key='-BROWSE-')],
              
              [sg.HSeparator()],
              [sg.Text('Set parameters', font='AnyFont 12 bold')],
              [sg.Text('Output Format:'), sg.Combo(values=('ClustalW with character counts', 'ClustalW',
                                                           'Pearson/FASTA', 'MSF', 'NEXUS', 'PHYLIP',
                                                           'SELEX', 'STOCKHOLM', 'VIENNA'),
                                                           default_value='ClustalW with character counts',
                                                           key = '-OUTPUTMSA-')],

              [sg.Text('\nDealign Input Sequences     MBED-Like Clustering Guide-Tree\
     Max HMM Iterations                       Distance Matrix')],
              [sg.Combo(values=('yes', 'no'), default_value='no', key='-DEALIGN-', size=(20,0)),
               sg.Combo(values=('yes', 'no'), default_value='yes', key='-MBED-', size=(27,0)),
               sg.Combo(values=('default', 0,1,2,3,4,5), default_value='default', key='-HMMITERATIONS-', size=(26,0)),
               sg.Combo(values=('yes', 'no'), default_value='no', key='-DISMATOUT-', size=(20,0))],

              [sg.Text('Max Guide Tree Iterations    MBED-Like Clustering Iteration\
         Number of Combined Iterations       Guide Tree')],
              [sg.Combo(values=('default', 0,1,2,3,4,5), default_value='default', key='-GTITERATIONS-' ,size=(20,0)),
               sg.Combo(values=('yes', 'no'), default_value='yes', key='-MBEDITERATION-', size=(27,0)),
               sg.Combo(values=('default(0)', 1,2,3,4,5), default_value='default(0)', key='-ITERATIONS-', size=(26,0)),
               sg.Combo(values=('yes', 'no'), default_value='yes', key='-GUIDETREEOUT-', size=(20,0))],

              [sg.Text('Order')],
              [sg.Combo(values=('aligned', 'input'), default_value='aligned', key='-ORDER-', size=(20,0))],
              
              [sg.Text('\n\n\t\t\t\t\t  '),
               sg.Button('Execute MSA', font='AnyFont, 13')],
              [sg.Text('\t\t\t\t\t             '),
               sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, key='-GIF1-',
                        enable_events=True, visible=True)],

              [sg.Button('< Back', font='AnyFont, 10', key='-B2-'),
               sg.Text('\t\t\t\t\t\t\t\t\t\t     '),
               sg.Button('Next >', font='AnyFont, 10', key='-N2-')]]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE TREE TAB ================================================================================
#===================================================================================================================
tree_layout = [[sg.Text('This is the Tree layout')],
               [sg.Button('< Back', font='AnyFont, 10', key='-B3-')]]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE LOG AND THE OUTPUT ======================================================================
#===================================================================================================================
# Define the layout of the log tab and the output
log_layout = [[sg.Text('Output', font='AnyFont 18')],
              [sg.Multiline(size=(115,30), font='Courier 8', key='-OUTPUT-', autoscroll=True)],
              [sg.Text('Event logging [LOG]', font='AnyFont 18')],
              [sg.Multiline(size=(115,15), font='Courier 8',
                            write_only=True,
                            reroute_stdout=True, reroute_stderr=True,
                            echo_stdout_stderr=True, autoscroll=True,
                            auto_refresh=True)],
              [sg.Text('\n\n\n\t\t\t\t\t      '),sg.Button('Exit', font='AnyFont, 12')]]
                            
# Create the main layout -------------------------------------------------------------------------------------------
layout = [[sg.MenubarCustom(menu_def, key='-MENU-',
                            font='Courier 15', tearoff=True)],
          [sg.Text('Alignment Navigated Search Organizer',
                   justification='center', font='AnyFont 20 bold',
                   relief=sg.RELIEF_RAISED,
                   enable_events=True, expand_x=True)],

          [sg.Column(
                [[sg.TabGroup(
                    [[sg.Tab('START', intro_layout, key='-START_TAB-'),
                      sg.Tab('BLAST', blast_layout, key='-BLAST_TAB-'),
                      sg.Tab('MSA', msa_layout, key='-MSA_TAB-'),
                      sg.Tab('TREE', tree_layout, key='-TREE_TAB-')]],
                      size=(750,900), expand_y=True, key='-TABGROUP-'
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
                   size=(1500,900), use_custom_titlebar=True,
                   finalize=True, keep_on_top=True)            # SET THIS ON TRUE AGAIN IF THE BLAST
    
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
while True:
    event, values = window.read(timeout=100)

    # Log every interaction with the Graphical User Interphase
    if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
        print('=========== Event = ', event, ' ============ ')
        print('----- Values Directory (key=value) -----')
        # for key in values:
        #     print(key, ' = ', values[key])
    
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
    
    # if event == 'Dark mode':
    #     if sg.theme('LightBrown2'):
    #         sg.theme('DarkBlue3')
    #     else:
    #         sg.theme('LightBrown2')
    
    # Buttons --------------------------------------------------------------------------
    if event == "-GET_STARTED-":
        print("[LOG] Went to the BLAST page")
        window['-BLAST_TAB-'].select()
    if event == "-B1-":
        print("[LOG] Went back to the START page")
        window['-START_TAB-'].select()
    if event == "-N1-":
        print("[LOG] Went to MSA page")
        window['-MSA_TAB-'].select()
    if event == "-B2-":
        print("[LOG Went back to the BLAST page]")
        window['-BLAST_TAB-'].select()
    if event == "-N2-":
        print("[LOG] Went to the TREE page")
        window['-TREE_TAB-'].select()
    if event == "-B3-":
        print("[LOG Went back to the MSA page]")
        window['-MSA_TAB-'].select()

    if event == "-BROWSE-":
        print("[LOG] Browsed after file")
        selected_file = values['-BROWSE-']
        window['-INFILE-'].update(selected_file)

    if event == "BLAST":
        print("[LOG] Clicked 'BLAST'")

        # Ask for input --------------------------------------------------------------
        program = values['-BLASTTYPE-']
        location = url + "?PROGRAM=" + program + "&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome"

        driver = (webdriver.Firefox())
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
        if values['-DB-'] == 'Reference proteins (refseq_protein)':
            values['-DB-'] = 'RR'
        if values['-DB-'] == 'Protein Data Bank proteins(pdb)':
            values['-DB-'] = 'pp'

        inputdatabasebutton = driver.find_element(By.ID, "DATABASE")
        inputdatabasebutton.click()
        inputdatabase = values['-DB-']
        database = driver.find_element(By.ID, "DATABASE")
        database.send_keys(inputdatabase)

        # Click on the drop down 'Algorithm paramters' Button
        Algorithmbutton = driver.find_element(By.ID, "btnDescrOver")
        Algorithmbutton.click()

        # Get information about the -MAXTS-
        if values['-MAXTS-'] == 10:
            values['-MAXTS-'] = 11
        if values['-MAXTS-'] == 50:
            values['-MAXTS-'] = 555
        if values['-MAXTS-'] == 100:
            values['-MAXTS-'] = 111
        if values['-MAXTS-'] == 5000:
            values['-MAXTS-'] = 55
           
        inputmaxbutton = driver.find_element(By.ID, "NUM_SEQ")
        inputmaxbutton.click()
        inputmax = values['-MAXTS-']
        max = driver.find_element(By.ID, "NUM_SEQ")
        max.send_keys(inputmax)

        # Get information about the -THRESHOLD-
        inputthreshold = values['-THRESHOLD-']
        threshold = driver.find_element(By.ID, "expect")
        threshold.clear()
        threshold.send_keys(inputthreshold)

        # Click on the BLAST Button
        blast = driver.find_element(By.CLASS_NAME, "blastbutton")
        blast.click()
        print('[LOG] Blast has started')

        max_wait_time = 99999
        update_interval = 5

        wait = WebDriverWait(driver, update_interval)

        try:
            driver.find_element(By.ID, "type-a")
            wait.until(EC.staleness_of(driver.find_element(By.ID, "type-a")))
        except:
            print('There went something wrong, try again later...')
            pass

        while max_wait_time > 0:
            try:
                download_button = wait.until(EC.element_to_be_clickable((By.ID, "btnDwnld")))
                download_button.click()
                print("[LOG] Clicked on the Download button")
                download_button2 = driver.find_element(By.ID, 'dwFST')
                download_button2.click()
                time.sleep(5)
                print("[LOG] The file has been downloaded")
                break
            
            except TimeoutException:
                max_wait_time -= update_interval
                continue
    
        # Display the output file
        file_path = os.path.expanduser("~/Downloads/seqdump.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
        window['-OUTPUT-'].update(file_content)

    if event == 'Execute MSA':
        print("[LOG] Clicked 'Execute MSA'")

        driver = (webdriver.Firefox())
        driver.get(urlclustal)

        # Cookies
        cookies = driver.find_element(By.ID, "data-protection-agree")
        cookies.click()

        # Input information about the type of the sequence -TYPE2SEQ-
        driver.find_element(By.ID, 'stype').send_keys(values['-TYPE2SEQ-'])

        # Input information about the query -QUERYMSA-
        driver.find_element(By.ID, 'sequence').send_keys(values['-QUERYMSA-'])

        # Input information about the output format -OUTPUTMSA-
        driver.find_element(By.ID, 'outfmt').send_keys(values['-OUTPUTMSA-'])

        # Click 'more options'
        options = driver.find_element(By.XPATH, '//*[@id="jd_toolSubmissionForm"]/div[2]/fieldset/p/a')
        options.click()

        # Input information about the dealign input sequence -DEALIGN-
        driver.find_element(By.ID, 'dealign').send_keys(values['-DEALIGN-'])

        # Input information about the MBED-like clustering guide-tree -MBED-
        driver.find_element(By.ID, 'mbed').send_keys(values['-MBED-'])

        # Input information about the max HMM iterations -HMMITERATIONS-
        driver.find_element(By.ID, 'hmmiterations').send_keys(values['-HMMITERATIONS-'])

        # Input information about the distance matrix -DISMATOUT-
        driver.find_element(By.ID, 'dismatout').send_keys(values['-DISMATOUT-'])

        # Input information about the max guide tree iterations -GTITERATIONS-
        driver.find_element(By.ID, 'gtiterations').send_keys(values['-GTITERATIONS-'])

        # Input information about the MBED-like clustering iteration -MBEDITERATION-
        driver.find_element(By.ID, 'mbediteration').send_keys(values['-MBEDITERATION-'])

        # Input information about the number of combined iterations -ITERATIONS-
        driver.find_element(By.ID, 'iterations').send_keys(values['-ITERATIONS-'])

        # Input information about the number of the guide tree -GUIDETREEOUT-
        driver.find_element(By.ID, 'guidetreeout').send_keys(values['-GUIDETREEOUT-'])

        # Input information about the number of the order -ORDER-
        driver.find_element(By.ID, 'order').send_keys(values['-ORDER-'])

        # Click on the Execute Multiple Aglinment Button
        ExecuteMSA = driver.find_element(By.XPATH, '//*[@id="jd_submitButtonPanel"]/input')
        ExecuteMSA.click()
        print('[LOG] MSA has started')

# window.close()