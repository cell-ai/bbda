import pandas as pd

def diamond(file):
  '''
  processes to df, a file generated from diamond blastp
  '''
  df = pd.read_csv(file, sep = "\t", header = None, names = ["qseqid", "qlen", "sseqid", "slen", "salltitles", "pident", "length", "mismatch", 
  "gapopen", "qstart", "qend", "sstart", "send", "qcovhsp", "evalue", "bitscore"]
  return df


def interproscan(file, go = True, pathway = True):
  '''
  processes to df, a file generated from interproscan search
  '''
  if go, pathway:
  interpro_df = pd.read_csv("concat_ro.refseq_serine.fasta.tsv", sep = "\t", header = None,
                           names = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                                   "e-value", "type", "date", "ipr", "ipr_desc", "go", "pathway"])
  else:
    if go:
      interpro_df = pd.read_csv("concat_ro.refseq_serine.fasta.tsv", sep = "\t", header = None,
                           names = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                                   "e-value", "type", "date", "ipr", "ipr_desc", "go"])
    if pathway:
      interpro_df = pd.read_csv("concat_ro.refseq_serine.fasta.tsv", sep = "\t", header = None,
                           names = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                                 "e-value", "type", "date", "ipr", "ipr_desc", "pathway"])
    else:
      interpro_df = pd.read_csv("concat_ro.refseq_serine.fasta.tsv", sep = "\t", header = None,
                     names = ["qseqid", "md5", "len", "db", "pfam_id", "pfam_desc", "start", "end",
                           "e-value", "type", "date", "ipr", "ipr_desc"])
