# pacybara_prep
Python script for taking a spreadsheet with sample information and converting it into parameterfiles for processing PacBio data with Pacybara
Note: I install dependencies and run this in my "pacybara" conda environment
Dependencies: pandas, pytz, python-dateutil, argparse, datetime
Instructions:
1) Configure pacybara_setup.csv so that the first column has the gene name, the second has the assay type, the third has the name of the fragment of the gene that mutated (usually nterm or cterm), fiveprime has the region that is 5' of the mutated sequence, target is the mutated region, and threeprime is 3' of the mutated region. It's important not to change the names of the columns.
2) Put the pacybara_setup.csv and make_parameter.py into the same directory
3) In the command line in that same directory type: chmod +x make_paramter.py
     -this gives permission for the script to run
4) In the command line type: python make_parameter.py pacybara_setup.csv


