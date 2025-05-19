# pip install pandas
# pip install pytz python-dateutil
import pandas as pd
import argparse
from datetime import datetime

# Parse command-line argument
parser = argparse.ArgumentParser(description="Generate Pacybara parameter files from a CSV.")
parser.add_argument("input_csv", help="Path to the input CSV file with gene, assay, fragment, fiveprime, target, threeprime columns")
args = parser.parse_args()

# Get today's date in YYYYMMDD format
today = datetime.today().strftime('%Y%m%d')

# Read CSV
df = pd.read_csv(args.input_csv)

# Template string
template = """#########################
#Pacybara parameter file
#########################

#BEGIN ARGUMENTS
#Experiment title
TITLE={title}
# Long read sequencing input file (fastq.gz)
INFASTQ=fastq.gz
# Workspace directory
WORKSPACE={title}
# The barcode degeneracy sequence used in the amplicon below
BARCODE=NNNNNNNNNNNNNNNN
# The start position of the ORF in the amplicon below (1-based)
ORFSTART={orfstart}
# The end position of the ORF in the amplicon below (1-based)
ORFEND={orfend}
# The maximum number of low-quality bases allowed in a given barcode.
MAXQDROPS=4
# The minimum average quality score allowed in a given barcode.
MINBCQ=32
#The minimum Jaccard coefficient (relative overlap of variants) for a cluster merge
MINJACCARD=0.2
#The minimum number of variants two cluster need to have in common to merge
MINMATCHES=1
#The maximum number of errors allowed between two barcode reads
MAXDIFF=1
#The minimum Q-score for a variant basecall to be considered real based on a single read alone
MINQUAL=27
#Cluster based on which barcodes? uptag, downtag, or virtual
CLUSTERMODE=uptag
#END ARGUMENTS

#BEGIN AMPLICON SEQUENCE
>{seq_title}
{amplicon}
#END AMPLICON SEQUENCE
"""

# Generate one .txt per row
for _, row in df.iterrows():
    gene = row["gene"]
    assay = row["assay"]
    fragment = row["fragment"]
    fiveprime = row["fiveprime"]
    target = row["target"]
    threeprime = row["threeprime"]

    full_sequence = f"{fiveprime}{target}{threeprime}"
    orfstart = len(fiveprime) + 1
    orfend = len(fiveprime) + len(target)

    title = f"{today}_{gene}_{assay}_{fragment}"
    seq_title = f"{gene}_{assay}_{fragment}"

    output = template.format(
        title=title,
        orfstart=orfstart,
        orfend=orfend,
        seq_title=seq_title,
        amplicon=full_sequence
    )

    filename = f"{title}.txt"
    with open(filename, "w") as f:
        f.write(output)

    print(f"Generated: {filename}")
