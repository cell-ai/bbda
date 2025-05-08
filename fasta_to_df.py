from Bio import SeqIO
import re
import pandas as pd

def fasta_to_df(fasta_file):
    records = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        # Parse protein name and organism from the description
        match = re.match(r"(\S+)\s+(.*)\s+\[(.+)\]$", record.description)
        if match:
            prot_id, prot_name, organism = match.groups()
        else:
            prot_id = record.id
            prot_name = ""
            organism = ""

        records.append({
            "id": prot_id,
            "sequence": str(record.seq),
            "description": record.description,
            "protein_name": prot_name,
            "organism": organism
        })
    return pd.DataFrame(records)


def df_to_fasta(output_file, fasta_df)
    with open(output_file, 'w') as fasta_file:
        for _, row in fasta_df.iterrows():
            header = row['header']
            sequence = row['sequence']
            fasta_file.write(f'>{header}\n{sequence}\n')
