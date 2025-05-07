import pandas as pd

def read_diamond_output(file):
  '''
  processes to df, a file generated from diamond blastp
  '''
  df = pd.read_csv(file, sep = "\t", header = None, names = ["qseqid", "qlen", "sseqid", "slen", "salltitles", "pident", "length", "mismatch", 
  "gapopen", "qstart", "qend", "sstart", "send", "qcovhsp", "evalue", "bitscore"]
  return df
