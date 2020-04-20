from io import StringIO
from typing import Optional

import requests
import pandas as pd

from covid19.file_helpers import path
from covid19.models import Genome


def parse_response(response: str) -> pd.DataFrame:
    """
    Parse genome data in .fasta format into a pandas data frame of Genome objects.
    """
    buf = StringIO(response)
    genomes = []
    genome = None
    skip = False
    skip_stats = {
        True: 0,
        False: 0,
    }

    for line in buf:
        if line.startswith('>'):
            if genome:
                genomes.append(genome)

            values = [value.strip() for value in line[1:].split('|')]
            skip = values[-1].strip().lower() != 'complete genome'
            skip_stats[skip] += 1

            if skip:
                continue

            id, name = values[:2]
            args = values[2:-1]
            genome = Genome(id, name, '', args)
        elif genome and not skip:
            genome.append(line)

    if skip_stats[True]:
        print(f'Skipped {skip_stats[True]}/{skip_stats[True] + skip_stats[False]} incomplete sequences')

    return pd.DataFrame.from_records([g.to_dict() for g in genomes])


def download_genomes(fasta_file: Optional[str] = None) -> pd.DataFrame:
    """
    Download and parse the most recent SARS-CoV-2 genomes list from ncbi.nlm.nih.gov.

    :param fasta_file: If set, the method will save the downloaded genomes in FASTA format to the specified file.
    """
    url = 'https://www.ncbi.nlm.nih.gov/genomes/VirusVariation/vvsearch2/' + \
          '?q=*:*&fq={!tag=SeqType_s}SeqType_s:("Nucleotide")' + \
          '&fq=VirusLineageId_ss:(2697049)&cmd=download&sort=CreateDate_dt desc,SourceDB_s desc' + \
          '&dlfmt=fasta&fl=id,Definition_s,Nucleotide_seq'

    response = requests.get(url).text
    if fasta_file:
        fasta_file = path(fasta_file)
        with open(fasta_file, 'w') as f:
            f.write(response)

    return parse_response(response)


# vim:sw=4:ts=4:et:
