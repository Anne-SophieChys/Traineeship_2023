#!/usr/bin/python3front
####################################################################################################################
####################################################################################################################
#                                            Graphical User Interphase                                             #
####################################################################################################################
####################################################################################################################

# Installations ----------------------------------------------------------------------------------------------------
import importlib
import subprocess

# list of packages to check and install
packages = {
    'PySimpleGUI': '4.60.4',
    'pyautogui': '0.9.54',
    'ete3': '3.1.3'
    }

for package, version in packages.items():
    try:
        importlib.import_module(package)
        print(f"{package} v{version} is already installed")

    except ImportError:
        subprocess.check_call(['pip', 'install', f"{package}=={version}"])
        print(f"{package} v{version} has been installed")

# Load the packages ------------------------------------------------------------------------------------------------
import PySimpleGUI as sg
from PIL import Image, ImageTk
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

imageDocument_pah = os.path.join(script_dir, "./Brand/Documentimage.jpg")
size = (102,102)
im5 = Image.open(imageDocument_pah)
im5 = im5.resize(size, resample=Image.BICUBIC)

imageTree_path = os.path.join(script_dir, "./Brand/Tree.png")
size = (100,142)
im6 = Image.open(imageTree_path)
im6 = im6.resize(size, resample=Image.BICUBIC)

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
                 sg.Text('       Basic Local Alignment Search Tool (BLAST)', font='AnyFont 18')],

                [sg.Text('BLAST is a widely used bioinformatics algorithm and software tool for \
sequence similarity searching. It is performed to compare a query sequence against a database of \
known sequences to identify similar sequences and infer functional or evolutionary relationships.\
\n\nThe main purpose of performing a BLAST search is to determine the similarity between a query \
sequence and sequences in a database. BLAST uses an algorithm that rapidly aligns the query \
sequence with sequences in the database and calculates a similarity score. This score indicates \
the degree of sequence similarity or homology between the query and database sequences.',
size=(105,None), expand_x=True)],
                
                [sg.HSeparator()],

                [sg.Text('\t\t\t'),
                 sg.Button('blastn', font='AnyFont, 10', key='-BLASTN-', button_color=('#475841', 'white')),
                 sg.Button('blastp', font='AnyFont, 10', key='-BLASTP-'),
                 sg.Button('blastx', font='AnyFont, 10', key='-BLASTX-'),
                 sg.Button('tblastn', font='AnyFont, 10', key='-TBLASTN-'),
                 sg.Button('tblastx', font='AnyFont, 10', key='-TBLASTX-')],

                [sg.Text('Enter Query Sequence', font='AnyFont 12 bold')],
                [sg.Text('Enter accession number(s) or FASTA sequence(s)', font='AnyFont 9 bold')],
                [sg.Multiline(key= '-QUERY-', size=(111,5))],

                [sg.Text('Or, upload file', font='AnyFont 9 bold'),
                sg.VSeparator(),
                sg.Input(enable_events=True, key='-INFILE-', expand_x=True, default_text="No file selected...", readonly=True),
                sg.FileBrowse(key='-FILEUPLOADBLAST-'),
                sg.Button('Clear', key='-CLEARBLAST-')],

                [sg.Text('Job Title\t          ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Input(key='-JOBTITLE-', border_width=0)],

                [sg.Text('Database          ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Combo(values=('Nucleotide collection (nr/nt)',
                                  'RefSeq Select RNA sequences (refseq_select)',
                                  'Reference RNA sequences (refseq_rna)',
                                  'RefSeq Representative genomes (refseq_representative_genomes)',
                                  'RefSeq Genome Database (refseq_genomes)',
                                  'Whole-genome shotgun contigs (wgs)',
                                  'Expressed sequence tags (est)',
                                  'Sequence Read Archive (SRA)',
                                  'Transcriptome Shotgun Assembly (TSA)',
                                  'Targeted Loci(TLS)',
                                  'High throughput genomic sequences (HTGS)',
                                  'Patent sequences(pat)',
                                  'PDB nucleotide database (pdb)',
                                  'Human RefSeqGene sequences(RefSeq_Gene)',
                                  'Genomic survey sequences (gss)',
                                  'Sequence tagged sites (dbsts)'),
                                  default_value='Nucleotide collection (nr/nt)',
                                  key='-DBBLASTN-', readonly=True, visible=True),

                 sg.Combo(values=('Non-redundant protein sequences (nr)',
                                  'RefSeq Select proteins (refseq_select)',
                                  'Reference proteins (refseq_protein)',
                                  'Model Organisms (landmark)',
                                  'UniProtKB/Swiss-Prot(swissprot)',
                                  'Patented protein sequences(pataa)',
                                  'Protein Data Bank proteins(pdb)',
                                  'Metagenomic proteins(env_nr)',
                                  'Transcriptome Shotgun Assembly proteins (tsa_nr)'),
                                  default_value='Non-redundant protein sequences (nr)',
                                  key='-DBBLASTP-', readonly=True, visible=False)],
                
                [sg.Text('Algorithm parameters', font='AnyFont 12 bold')],
                [sg.Text('Max target \nsequences        ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Combo(values=(10,50,100,200,250,500,1000,5000),
                          default_value='100',
                          key='-MAXTS-',
                          readonly=True)],

                [sg.Text('Threshold         ', font='AnyFont 9 bold'),
                 sg.VSeparator(),
                 sg.Input(key='-THRESHOLD-', size=(5,0), default_text=0.05)],

                [sg.Text('\n\n\n\n\n\n\n')],

                [sg.Button('< Back', font='AnyFont, 10', key='-B0-'),
                 sg.Text('\t\t\t\t\t\t\t\t\t'),
                 sg.Button('CUSTOMIZE BLAST >', font='AnyFont, 10', key='-N1-')]
                ]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE Customize TAB ===========================================================================
#===================================================================================================================
customize_layout = [[sg.Image(size=(102,102), key='-IMAGE5-'),
                        sg.VSeparator(),
                        sg.Text('       Customize of the Downloaded Document', font='AnyFont 18')],
                       [sg.Text('The "Customize" tab in the ANSO application provides users with convenient \
filters to refine their results obtained from the BLAST NCBI database. Users can customize their sequence analysis \
by adjusting parameters such as the number of sequences, percent identity range, E-value threshold, and query \
coverage. These filters enable users to focus on a specific subset of sequences that meet their desired \
criteria, ensuring that the final results are relevant and statistically significant. By fine-tuning these \
parameters, researchers can efficiently extract valuable insights from their sequence analysis and streamline \
their bioinformatics workflows.', size=(105, None))],
                       
                       [sg.Text('Filter Results', font='AnyFont 12 bold')],
                       [sg.Text('Below filters can be set so the document that you downloaded from the BLAST \
can be customized. This customized document will be downloaded and used for the following MSA-step and for \
building the phylogenetic tree', size=(105,None))],
                    
                       [sg.HSeparator()],

                       [sg.Text('Number of sequences', font='AnyFont 9 bold')],
                       [sg.Text('Specify the number of sequences if it is not available on NCBI:'),
                        sg.VSeparator(),
                        sg.Input(key='-AMOUNTSEQ-', border_width=0, size=(7,0))],
                        
                       [sg.Text('Percent Identity', font='AnyFont 9 bold')],                       
                       [sg.Text('Specify the minimum and maximum percent identity:\t        '),
                        sg.VSeparator(),
                        sg.Input(key='-PERCENTIDMIN-', border_width=0, size=(7,0), default_text=' '),
                        sg.Text('to'),
                        sg.Input(key='-PERCENTIDMAX-', border_width=0, size=(7,0))], 

                       [sg.Text('E value', font='AnyFont 9 bold')],                       
                       [sg.Text('Specify the minimum and maximum E value:\t\t        '),
                        sg.VSeparator(),
                        sg.Input(key='-EVALUEMIN-', border_width=0, size=(7,0)),
                        sg.Text('to'),
                        sg.Input(key='-EVALUEMAX-', border_width=0, size=(7,0))],

                        [sg.Text('Query Coverage', font='AnyFont 9 bold')],                       
                        [sg.Text('Specify the minimum and maximum query coverage:\t        '),
                        sg.VSeparator(),
                        sg.Input(key='-QUERYCOVERAGEMIN-', border_width=0, size=(7,0)),
                        sg.Text('to'),
                        sg.Input(key='-QUERYCOVERAGEMAX-', border_width=0, size=(7,0))],

                        [sg.Text('\n\n')],
                        # [sg.Text('Organism', font='AnyFont 9 bold')],                       
                        # [sg.Text('Specify the organism:\t\t\t\t        '),
                        # sg.VSeparator(),
                        # sg.Input(key='-ORGANISMID-', border_width=0)],

                       [sg.Text('\t\t\t\t\t        '),
                        sg.Button('BLAST', font='AnyFont, 13'),
                        sg.Text('\n\n\n\n\n\n\n\n\n\n\n\n')],

                       [sg.Button('< Back', font='AnyFont, 10', key='-B1-'),
                        sg.Text('\t\t\t\t\t\t\t\t\t\t     '),
                        sg.Button('Next >', font='AnyFont, 10', key='-N2-')]
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
                        size=(9,0), enable_events=True, readonly=True)],
              [sg.Text('Enter Query Sequences', font='AnyFont 12 bold')],
              [sg.Text('Support Formats: FASTA, GCG, EMBL (Nucleotide only), GenBank, PIR/NBRF, PHILIP or UniProtKB/Swiss-Prot (Protein only)', font='AnyFont 9 bold')],
              [sg.Multiline(key= '-QUERYMSA-', size=(111,6))],
              [sg.Text('Or, upload file', font='AnyFont 9 bold'),
               sg.VSeparator(),
               sg.Input(key='-FILENAMEMSA-', enable_events=True, expand_x=True, default_text="No file selected...", readonly=True),
               sg.FileBrowse(key='-FILEUPLOADMSA-'),
               sg.Button('Clear', key='-CLEARMSA-')],
              
              [sg.HSeparator()],
              [sg.Text('Set parameters', font='AnyFont 12 bold')],
              [sg.Text('Output Format:'), sg.Combo(values=('ClustalW with character counts', 'ClustalW',
                                                           'Pearson/FASTA', 'MSF', 'NEXUS', 'PHYLIP',
                                                           'SELEX', 'STOCKHOLM', 'VIENNA'),
                                                           default_value='ClustalW with character counts',
                                                           key = '-OUTPUTMSA-', readonly=True)],

              [sg.Text('\nDealign Input Sequences     MBED-Like Clustering Guide-Tree\
     Max HMM Iterations                       Distance Matrix')],
              [sg.Combo(values=('yes', 'no'), default_value='no', key='-DEALIGN-', size=(20,0), readonly=True),
               sg.Combo(values=('yes', 'no'), default_value='yes', key='-MBED-', size=(27,0), readonly=True),
               sg.Combo(values=('default', 0,1,2,3,4,5), default_value='default', key='-HMMITERATIONS-', size=(26,0), readonly=True),
               sg.Combo(values=('yes', 'no'), default_value='no', key='-DISMATOUT-', size=(20,0), readonly=True)],

              [sg.Text('Max Guide Tree Iterations    MBED-Like Clustering Iteration\
         Number of Combined Iterations       Guide Tree')],
              [sg.Combo(values=('default', 0,1,2,3,4,5), default_value='default', key='-GTITERATIONS-' ,size=(20,0), readonly=True),
               sg.Combo(values=('yes', 'no'), default_value='yes', key='-MBEDITERATION-', size=(27,0), readonly=True),
               sg.Combo(values=('default(0)', 1,2,3,4,5), default_value='default(0)', key='-ITERATIONS-', size=(26,0), readonly=True),
               sg.Combo(values=('yes', 'no'), default_value='yes', key='-GUIDETREEOUT-', size=(20,0), readonly=True)],

              [sg.Text('Order')],
              [sg.Combo(values=('aligned', 'input'), default_value='aligned', key='-ORDER-', size=(20,0), readonly=True)],
              
              [sg.Text('\n\n\t\t\t\t\t         '),
               sg.Button('MSA', font='AnyFont, 13'),
               sg.Text('\n\n\n\n\n\n\n\n')],


              [sg.Button('< Back', font='AnyFont, 10', key='-B2-'),
               sg.Text('\t\t\t\t\t\t\t\t\t\t     '),
               sg.Button('Next >', font='AnyFont, 10', key='-N3-')]]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE TREE TAB ================================================================================
#===================================================================================================================
tree_layout = [[sg.Image(size=(100,142), key='-IMAGE6-'),
                sg.VSeparator(),
                sg.Text('       Building Phylogenetic Tree', font='AnyFont 18')],
               [sg.Text('In addition to its existing functionalities, the ANSO application also \
offers the capability to build phylogenetic trees using the neighborhood joining method with \
Clustal Omega. This new feature allows users to analyze the evolutionary relationships among their \
sequences and gain insights into their genetic similarities and divergence. By integrating the \
tree-building functionality, ANSO provides a comprehensive toolkit for sequence analysis and \
interpretation.', size=(105,None))],

              [sg.HSeparator()],

              [sg.Frame('Visual Tree Output', [[sg.Multiline(size=(103,21), background_color='#F7F3EC', key="-VISUALTREE-",
                                                     autoscroll=False)]])],

              [sg.Text('\n\n\n\t\t\t\t\t       '),
               sg.Button('BUILD', font='AnyFont, 13'),
               sg.Text('\n\n\n\n\n\n\n\n\n\n\n')],

               [sg.Button('< Back', font='AnyFont, 10', key='-B3-')]]

#===================================================================================================================
# DEFINE THE LAYOUT OF THE LOG AND THE OUTPUT ======================================================================
#===================================================================================================================
# Define the layout of the log tab and the output
output_layout = [[sg.Text('\t\t              OUTPUT', font='AnyFont 18')],
                 [sg.Multiline(size=(150,48), font='Courier 8', key='-OUTPUT-', autoscroll=False,
                               write_only=True, auto_refresh=True)],
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
                      sg.Tab('CUSTOMIZE', customize_layout, key='-CUSTOMIZE_TAB-'),
                      sg.Tab('MSA', msa_layout, key='-MSA_TAB-'),
                      sg.Tab('TREE', tree_layout, key='-TREE_TAB-')]],
                      size=(750,900), expand_y=True, key='-TABGROUP-'
                )]], sbar_relief=sg.RELIEF_RAISED),

          sg.Column(
                    [[sg.Frame('', output_layout, border_width=0,
                               pad=((0,0),(20,0)))]],
                               expand_y=True)
                ]]

####################################################################################################################
####################################################################################################################
#                                                    def main                                                      #
####################################################################################################################
####################################################################################################################
# Main functions
def main():
    make_window(sg.theme('LightBrown2'))

# Create the window ------------------------------------------------------------------------------------------------
window = sg.Window('Graphical User Interphase', layout,
                   grab_anywhere=True,
                   size=(1520,900), use_custom_titlebar=True,
                   finalize=True, keep_on_top=False)            # SET THIS ON TRUE AGAIN IF THE BLAST
    
# Convert im to ImageTK.PhotoImage after window finalized
image = ImageTk.PhotoImage(image=im)
image2 = ImageTk.PhotoImage(image=im2)
image3 = ImageTk.PhotoImage(image=im3)
image4 = ImageTk.PhotoImage(image=im4)
image5 = ImageTk.PhotoImage(image=im5)
image6 = ImageTk.PhotoImage(image=im6)

window['-IMAGE-'].update(data=image)
window['-IMAGE2-'].update(data=image2)
window['-IMAGE3-'].update(data=image3)
window['-IMAGE4-'].update(data=image4)
window['-IMAGE5-'].update(data=image5)
window['-IMAGE6-'].update(data=image6)

####################################################################################################################
####################################################################################################################
#                                                 Define function                                                  #
####################################################################################################################
####################################################################################################################
# Define the latest file to display in the output
# def get_latest_file(directory):
#     files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
#     if not files:
#         return None
#     latest_file = max(files, key=os.path.getmtime)
#     return latest_file

####################################################################################################################
####################################################################################################################
#                                                   Event loop                                                     #
####################################################################################################################
####################################################################################################################
import glob                                                         # Usage of glob module to use wildcard patterns in filenames
import pyautogui                                                    # Send keys like CONTROL and SHIFT to the web
from ete3 import Tree                                               # To build the Tree
from PIL import Image
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
                    'Tool :: tkinter v8.6',
                    'url :: \"https://github.com/PySimpleGUI/PySimpleGUI\"',
                    keep_on_top=True)
    
    # if event == 'Dark mode':
    #     if sg.theme('LightBrown2'):
    #         sg.theme('DarkBlue3')
    #     else:
    #         sg.theme('LightBrown2')

    # Buttons ------------------------------------------------------------------------------------------------------
    if event == "-GET_STARTED-":
        print("[LOG] Went to the BLAST page")
        window['-BLAST_TAB-'].select()

    if event == "-N1-":
        print("[LOG] Went to CUSTOMIZE page")
        window['-CUSTOMIZE_TAB-'].select()

    if event == "-N2-":
        print("[LOG] Went to MSA page")
        window['-MSA_TAB-'].select()
        try:
            window['-OUTPUT-'].update(file_contentmsa)
        except:
            window['-OUTPUT-'].update('')

    if event == "-N3-":
        print("[LOG] Went to the TREE page")
        window['-TREE_TAB-'].select()

        correct_directory_treecode = os.path.expanduser("~/Downloads/")
        clustal_treecode_path = os.path.join(correct_directory_treecode, "clustalo*p1m.ph")
        matching_files_treecode = glob.glob(clustal_treecode_path)
        matching_files_treecode.sort(key=os.path.getmtime, reverse=True)

        if matching_files_treecode:
            latest_file = matching_files_treecode[0]

            with open(latest_file, 'r') as file:
                file_contenttreecode = file.read()
            window['-OUTPUT-'].update(file_contenttreecode)
        
        else:
            print("No matching files found...")


    if event == "-B0-":
        print("[LOG] Went back to the START page")
        window['-START_TAB-'].select()

    if event == '-B1-':
        print("[LOG] Went back to the BLAST page")
        window['-BLAST_TAB-'].select()

    if event == "-B2-":
        print("[LOG] Went back to the CUSTOMIZE page")
        window['-CUSTOMIZE_TAB-'].select()
        try:
            window['-OUTPUT-'].update(latest_matching_BlastfileForMSA)
        except:
            window['-OUTPUT-'].update('')

    if event == "-B3-":
        print("[LOG Went back to the MSA page]")
        window['-MSA_TAB-'].select()
        try:
            window['-OUTPUT-'].update(file_contentmsa)
        except NameError:
            window['-OUTPUT-'].update('')
        
    if event == "-CLEARBLAST-":
        window['-INFILE-'].update('')
        window['-QUERY-'].update('')

    if event == "-CLEARMSA-":
        window['-FILENAMEMSA-'].update('')
        window['-QUERYMSA-'].update('')

#===================================================================================================================
# DEFINE THE EVENTS OF THE BLAST LAYOUT ============================================================================
#===================================================================================================================
    select_button1 = '-BLASTN-'
    select_button2 = '-BLASTP-'
    select_button3 = '-BLASTX-'
    select_button4 = '-TBLASTN-'
    select_button5 = '-TBLASTX-'

    if event in ['-BLASTN-', '-BLASTP-', '-BLASTX-', '-TBLASTN-', '-TBLASTX-']:
        window[select_button1].update(button_color=('#475841', 'white'))
        window[select_button1].update(button_color=('white', '#475841'))
        window[select_button2].update(button_color=('#475841', 'white'))
        window[select_button2].update(button_color=('white', '#475841'))
        window[select_button3].update(button_color=('#475841', 'white'))
        window[select_button3].update(button_color=('white', '#475841'))
        window[select_button4].update(button_color=('#475841', 'white'))
        window[select_button4].update(button_color=('white', '#475841'))
        window[select_button5].update(button_color=('#475841', 'white'))
        window[select_button5].update(button_color=('white', '#475841'))
        window[event].update(button_color=('#475841', 'white'))
        select_button=event
   
    if event == '-BLASTN-':
        print('[LOG] The tab BLASTN is selected')
        programtype = 'blastn'
        window['-DBBLASTN-'].update(visible=True)
        window['-DBBLASTP-'].update(visible=False)

    if event == '-BLASTP-':
        print('[LOG] The tab BLASTP is selected')
        programtype = 'blastp'
        window['-DBBLASTN-'].update(visible=False)
        window['-DBBLASTP-'].update(visible=True)

    if event == '-BLASTX-':
        print('[LOG] The tab BLASTX is selected')
        programtype = 'blastx'
        window['-DBBLASTN-'].update(visible=False)
        window['-DBBLASTP-'].update(visible=True)

    if event == '-TBLASTN-':
        print('[LOG] The tab TBLASTN is selected')
        programtype = 'tblastn' 
        window['-DBBLASTN-'].update(visible=True)
        window['-DBBLASTP-'].update(visible=False)

    if event == '-TBLASTX-':
        print('[LOG] The tab TBLASTX is selected')
        programtype = 'tblastx' 
        window['-DBBLASTN-'].update(visible=True)
        window['-DBBLASTP-'].update(visible=False)

# Performing the BLAST ---------------------------------------------------------------------------------------------
    if event == "BLAST":
        print("[LOG] Started the 'BLAST'")

        
        popup_layout = [
            [sg.Text('Blasting... Please wait!',
                     font='AnyFont 12 bold', key='-POPUP-TEXT-')],

            [sg.Text('            ', key='-EMOJI_DREAMING_SPACE-'),
             sg.Image(data=sg.EMOJI_BASE64_DREAMING, visible=True, key='-EMOJI_DREAMING-'),
             sg.Text('       ', key='-EMOJI_HAPPY_SPACE-'),
             sg.Image(data=sg.EMOJI_BASE64_HAPPY_JOY, visible=False, key='-EMOJI_HAPPY-')],

            [sg.Text('      '),
             sg.Button('Finish', key='-POPUP-FINISH-', visible=False)]
            ]

        popup_window = sg.Window('Blast in progress', popup_layout, modal=True, finalize=True,
                                 keep_on_top=True, auto_size_text=True)

        for _ in range (1):
            popup_window['-EMOJI_DREAMING-'].update(visible=True)
            popup_window['-EMOJI_HAPPY-'].update(visible=False)


        # Ask for input --------------------------------
        # programtype = 'blastn'
        program = programtype
        location = url + "?PROGRAM=" + program + "&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome"
        print(location)
        driver = (webdriver.Firefox())
        driver.get(location)

        # Get information about the -QUERY-
        inputquery = values['-QUERY-']
        query = driver.find_element(By.ID, "seq")
        query.send_keys(inputquery)

        # Get information about the -FILEUPLOADBLAST-'
        inputfileblast = values['-FILEUPLOADBLAST-']
        print(inputfileblast)
        if inputfileblast:
            upload = driver.find_element(By.ID, "upl")
            upload.send_keys(inputfileblast)

        # Get information about the -JOBTITLE-
        inputjobtitle = values['-JOBTITLE-']
        jobtitle = driver.find_element(By.NAME, "JOB_TITLE")
        jobtitle.send_keys(inputjobtitle)

        # Get information about the -DBBLASTP-
        if values['-DBBLASTP-'] == 'Non-redundant protein sequences (nr)':
            values['-DBBLASTP-'] = 'N'
        if values['-DBBLASTP-'] == 'RefSeq Select proteins (refseq_select)':
            values['-DBBLASTP-'] = 'R'
        if values['-DBBLASTP-'] == 'Reference proteins (refseq_protein)':
            values['-DBBLASTP-'] = 'RR'
        if values['-DBBLASTP-'] == 'Model Organisms (landmark)':
            values['-DBBLASTP-'] = 'M'
        if values['-DBBLASTP-'] == 'UniProtKB/Swiss-Prot(swissprot)':
            values['-DBBLASTP-'] = 'U'
        if values['-DBBLASTP-'] == 'Patented protein sequences(pataa)':
            values['-DBBLASTP-'] = 'P'
        if values['-DBBLASTP-'] == 'Protein Data Bank proteins(pdb)':
            values['-DBBLASTP-'] = 'PP'
        if values['-DBBLASTP-'] == 'Metagenomic proteins(env_nr)':
            values['-DBBLASTP-'] = 'MM'
        if values['-DBBLASTP-'] == 'Transcriptome Shotgun Assembly proteins (tsa_nr)':
            values['-DBBLASTP-'] = 'T'

            
        # Get information about the -DBBLASTN-
        if values['-DBBLASTN-'] == 'Nucleotide collection (nr/nt)':
            values['-DBBLASTN-'] = 'N'
        if values['-DBBLASTN-'] == 'RefSeq Select RNA sequences (refseq_select)':
            values['-DBBLASTN-'] = 'R'
        if values['-DBBLASTN-'] == 'Reference RNA sequences (refseq_rna)':
            values['-DBBLASTN-'] = 'RR'
        if values['-DBBLASTN-'] == 'RefSeq Representative genomes (refseq_representative_genomes)':
            values['-DBBLASTN-'] = 'RRR'
        if values['-DBBLASTN-'] == 'RefSeq Genome Database (refseq_genomes)':
            values['-DBBLASTN-'] = 'RRRR'
        if values['-DBBLASTN-'] == 'Whole-genome shotgun contigs (wgs)':
            values['-DBBLASTN-'] = 'W'
        if values['-DBBLASTN-'] == 'Expressed sequence tags (est)':
            values['-DBBLASTN-'] = 'E'
        if values['-DBBLASTN-'] == 'Sequence Read Archive (SRA)':
            values['-DBBLASTN-'] = 'S'
        if values['-DBBLASTN-'] == 'Transcriptome Shotgun Assembly (TSA)':
            values['-DBBLASTN-'] = 'T'
        if values['-DBBLASTN-'] == 'Targeted Loci(TLS)':
            values['-DBBLASTN-'] = 'TT'
        if values['-DBBLASTN-'] == 'High throughput genomic sequences (HTGS)':
            values['-DBBLASTN-'] = 'H'
        if values['-DBBLASTN-'] == 'Patent sequences(pat)':
            values['-DBBLASTN-'] = 'P'
        if values['-DBBLASTN-'] == 'PDB nucleotide database (pdb)':
            values['-DBBLASTN-'] = 'PP'
        if values['-DBBLASTN-'] == 'Human RefSeqGene sequences(RefSeq_Gene)':
            values['-DBBLASTN-'] = 'HH'
        if values['-DBBLASTN-'] == 'Genomic survey sequences (gss)':
            values['-DBBLASTN-'] = 'G'
        if values['-DBBLASTN-'] == 'Sequence tagged sites (dbsts)':
            values['-DBBLASTN-'] = 'SS'

        inputdatabasebutton = driver.find_element(By.ID, "DATABASE")
        inputdatabasebutton.click()
        # BLAST P works because it is the standard
        inputdatabase = values['-DBBLASTP-']
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

        max_wait_time_filter = 99999
        max_wait_time_download = 99999
        update_interval = 5

        wait = WebDriverWait(driver, update_interval)

        try:
            driver.find_element(By.ID, "type-a")
            wait.until(EC.staleness_of(driver.find_element(By.ID, "type-a")))
        except:
            print('There went something wrong, try again later...')
            pass

        while max_wait_time_filter > 0:
            try:
#===================================================================================================================
# DEFINE THE EVENTS OF THE CUSTOMIZE LAYOUT ========================================================================
#===================================================================================================================
                
                # Input information about '-PERCENTIDMIN-':
                prcLow_element = wait.until(EC.presence_of_element_located((By.ID, 'prcLow')))
                prcLow_element.send_keys(values['-PERCENTIDMIN-'])
                # Input information about '-PERCENTIDMAX-':
                driver.find_element(By.ID, 'prcHigh').send_keys(values['-PERCENTIDMAX-'])
                # Input information about 'EVALUEMIN-':
                driver.find_element(By.ID, 'expHigh').send_keys(values['-EVALUEMAX-'])
                # Input information about '-EVALUEMIN-':
                driver.find_element(By.ID, 'expLow').send_keys(values['-EVALUEMIN-'])
                # Input information about '-EVALUEMAX-':
                driver.find_element(By.ID, 'expHigh').send_keys(values['-EVALUEMAX-'])
                # Input information about '-QUERYCOVERAGEMIN-':
                driver.find_element(By.ID, 'qcLow').send_keys(values['-QUERYCOVERAGEMIN-'])
                # Input information about '-QUERYCOVERAGEMAX-':
                driver.find_element(By.ID, 'qcHigh').send_keys(values['-QUERYCOVERAGEMAX-'])
                # Input information about '-ORGANISMID-':
                # driver.find_element(By.ID, 'qorganism').send_keys(values['-ORGANISMID-'])
                ExecuteFilter = driver.find_element(By.ID, 'btnFilter')
                time.sleep(1)
                ExecuteFilter.click()
                time.sleep(1)
                print('[LOG] Filtering has started')
                break
          
            except TimeoutException:
                max_wait_time_filter -= update_interval
                continue
        
        while max_wait_time_download > 0:
            try:
                # Download the file
                download_button = wait.until(EC.element_to_be_clickable((By.ID, "btnDwnld")))
                download_button.click()
                # time.sleep(3)
                print("[LOG] Clicked on the Download button")
                download_button2 = wait.until(EC.element_to_be_clickable((By.ID, 'dwFST')))
                download_button2.click()
                print("[LOG] The file has been downloaded")
                time.sleep(5)
                # driver.close()
                break

            except TimeoutException:
                max_wait_time_download -= update_interval
                continue
                
    #-------------------------------------------------------------------------------------------------
        # Choose the last downloaded/modified file
        correct_directory_BlastfileForMSA = os.path.expanduser("~/Downloads/")
        BlastfileForMSA_path = os.path.join(correct_directory_BlastfileForMSA, "*seqdump*")
        matching_BlastfileForMSA = glob.glob(BlastfileForMSA_path)
        matching_BlastfileForMSA.sort(key=os.path.getmtime, reverse=True)
        
        if matching_BlastfileForMSA:
            latest_matching_BlastfileForMSA = matching_BlastfileForMSA[0]
            amountsequences = int(values['-AMOUNTSEQ-'])

            if os.path.exists(latest_matching_BlastfileForMSA):
                with open(latest_matching_BlastfileForMSA, 'r+') as file:
                    lines = file.readlines()

                    sequence_indices = [i for i, line in enumerate(lines) if line.startswith('>')][:amountsequences+1]
                    
                    if len(sequence_indices) >= amountsequences+1:
                        lines = lines[:sequence_indices[amountsequences]+1]

                    lines = lines[:-1]
                    
                    file.seek(0)
                    file.truncate()

                    file.writelines(lines)

            window['-OUTPUT-'].update(''.join(lines))
        
        # Loading Ready ----------------------------------------------------------------------------------------------
        popup_window['-POPUP-TEXT-'].update('Blast completed!')
        popup_window['-POPUP-FINISH-'].update(visible=True)
        popup_window['-EMOJI_HAPPY-'].update(visible=True)
        popup_window['-EMOJI_HAPPY_SPACE-'].update(visible=True)
        popup_window['-EMOJI_DREAMING-'].update(visible=False)
        popup_window['-EMOJI_DREAMING_SPACE-'].update(visible=False)

        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event == '-POPUP-FINISH-' or popup_event == sg.WINDOW_CLOSED:
                popup_window.close()
                window['-MSA_TAB-'].select()
                
                if matching_BlastfileForMSA:
                    latest_matching_BlastfileForMSA = matching_BlastfileForMSA[0]
                    window['-FILENAMEMSA-'].update(latest_matching_BlastfileForMSA)

                break

            driver.quit()

#===================================================================================================================
# DEFINE THE EVENTS OF THE MSA LAYOUT ==============================================================================
#===================================================================================================================
    if event == 'MSA':
        print("[LOG] Clicked 'MSA'")

        # POPUP
        popup_layout = [
            [sg.Text('Performing MSA... Please wait!',
                     font='AnyFont 12 bold', key='-POPUP-TEXT-')],

            [sg.Text('                    ', key='-EMOJI_DREAMING_SPACE-'),
             sg.Image(data=sg.EMOJI_BASE64_DREAMING, visible=True, key='-EMOJI_DREAMING-'),
             sg.Text('       ', key='-EMOJI_HAPPY_SPACE-'),
             sg.Image(data=sg.EMOJI_BASE64_HAPPY_JOY, visible=False, key='-EMOJI_HAPPY-')],

            [sg.Text('      '),
             sg.Button('Finish', key='-POPUP-FINISH-', visible=False)]
            ]

        popup_window = sg.Window('MSA in progress', popup_layout, modal=True, finalize=True,
                                 keep_on_top=True, auto_size_text=True)

        for _ in range (1):
            popup_window['-EMOJI_DREAMING-'].update(visible=True)
            popup_window['-EMOJI_HAPPY-'].update(visible=False)

        # Perofrm the driver    
        driver = (webdriver.Firefox())
        driver.get(urlclustal)

        # Cookies
        cookies = driver.find_element(By.ID, "data-protection-agree")
        cookies.click()

        # Input information about the type of the sequence -TYPE2SEQ-
        driver.find_element(By.ID, 'stype').send_keys(values['-TYPE2SEQ-'])

        # Input information about the query -QUERYMSA-
        driver.find_element(By.ID, 'sequence').send_keys(values['-QUERYMSA-'])

        # Input information about the -FILEUPLOADMSA-'
        inputfilemsa = values['-FILENAMEMSA-']
        print(inputfilemsa)
        if inputfilemsa:
            uploadmsa = driver.find_element(By.ID, "upfile")
            uploadmsa.send_keys(inputfilemsa)

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

        max_wait_time_msa = 99999
        update_interval_msa = 5

        wait_msa = WebDriverWait(driver, update_interval_msa)

        try:
            driver.find_element(By.ID, "alignmentContent")
            wait_msa.until(EC.staleness_of(driver.find_element(By.ID, "alignmentContent")))
        except:
            print('There went something wrong, try again later...')
            pass
        
        while max_wait_time_msa > 0:
            try:
                # Download the files
                summary_button = wait_msa.until(EC.element_to_be_clickable((By.ID, "summary")))
                summary_button.click()

                # Download the first file
                clustal_num = wait_msa.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="links"]/dl/dd[3]/a')))
                clustal_num.click()

                # Download the second file
                clustal_treecodepage = wait_msa.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="links"]/dl/dd[5]/a')))
                clustal_treecodepage.click()
                time.sleep(2)

                pyautogui.hotkey('ctrl', 's', interval=0.25)
                pyautogui.press('enter')
                print('[LOG] The files have been downloaded')
                driver.back()

                # A picture of the tree is downloaded
                clustal_PT = wait_msa.until(EC.element_to_be_clickable((By.ID, "phylotree")))
                clustal_PT.click()

                image_tree = driver.find_element(By.ID, "tv_tree")
                image_tree.screenshot("image_tree.png")
                cwd = os.getcwd()
                downloads_dir = os.path.expanduser('~/Downloads')
                new_path = os.path.join (downloads_dir, 'image_tree.png')
                import shutil
                shutil.move('image_tree.png', new_path)
                driver.close()
                break

            except TimeoutException:
                max_wait_time_msa -= update_interval_msa
                continue
        
        correct_directory = os.path.expanduser("~/Downloads/")
        clustal_msa_path = os.path.join(correct_directory, "clustalo*p1m.clustal_num")
        matching_files = glob.glob(clustal_msa_path)
        matching_files.sort(key=os.path.getmtime, reverse=True)

        if matching_files:
            latest_file = matching_files[0]

            with open(latest_file, 'r') as file:
                file_contentmsa = file.read()

            window['-OUTPUT-'].update(file_contentmsa)
        
        else:
            print("No matching files found...")
    
        # Loading Ready ----------------------------------------------------------------------------------------------
        popup_window['-POPUP-TEXT-'].update('MSA completed!')
        popup_window['-POPUP-FINISH-'].update(visible=True)
        popup_window['-EMOJI_HAPPY-'].update(visible=True)
        popup_window['-EMOJI_HAPPY_SPACE-'].update(visible=True)
        popup_window['-EMOJI_DREAMING-'].update(visible=False)
        popup_window['-EMOJI_DREAMING_SPACE-'].update(visible=False)

        while True:
            popup_event, popup_values = popup_window.read()
            if popup_event == '-POPUP-FINISH-' or popup_event == sg.WINDOW_CLOSED:
                popup_window.close()
                break

    if event == 'BUILD':
        print("[LOG] Building the TREE")
        correct_directory_treeviewer = os.path.expanduser("~/Downloads/")
        clustal_treeviewer_path = os.path.join(correct_directory_treeviewer, "clustalo*p1m.ph")
        matching_files_treeviewer = glob.glob(clustal_treeviewer_path)
        matching_files_treeviewer.sort(key=os.path.getmtime, reverse=True)

        if matching_files_treeviewer:
            latest_file_treeviewer = matching_files_treeviewer[0]

            unrooted_tree = Tree(latest_file_treeviewer)
            tree_file = "unrooted_tree.nw"
            with open (tree_file, 'w') as file:
                print(unrooted_tree, file=file)

            with open("unrooted_tree.nw", 'r') as file:
                file_contenttreeviewer = file.read()
            window['-VISUALTREE-'].update(file_contenttreeviewer)
        
        else:
            print("No matching files found...")
        
# window.close()
