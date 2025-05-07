import pandas as pd

def diamond(file):
  '''
  processes to df, a file generated from diamond blastp
  '''
  diamond_df = pd.read_csv(file, sep = "\t", header = None, names = ["qseqid", "qlen", "sseqid", "slen", "salltitles", "pident", "length", "mismatch", 
  "gapopen", "qstart", "qend", "sstart", "send", "qcovhsp", "evalue", "bitscore"]
  return diamond_df


def interproscan(file, go=True, pathway=True):
    '''
    Processes to df, a file generated from InterProScan search
    '''
    if go and pathway:
        colnames = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                    "e-value", "type", "date", "ipr", "ipr_desc", "go", "pathway"]
    elif go:
        colnames = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                    "e-value", "type", "date", "ipr", "ipr_desc", "go"]
    elif pathway:
        colnames = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                    "e-value", "type", "date", "ipr", "ipr_desc", "pathway"]
    else:
        colnames = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                    "e-value", "type", "date", "ipr", "ipr_desc"]
    
    interpro_df = pd.read_csv(file, sep="\t", header=None, names=colnames)
    return interpro_df
