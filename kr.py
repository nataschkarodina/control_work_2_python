from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

records = SeqIO.parse("classwork2.fasta", format="fasta")

with open ('new_fasta.fasta', 'w') as new_fasta_out:
    for rec in records:
        name, sequence = rec.id, str(rec.seq)
        print(name, sequence)
        result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    print('>',alignment.title, sequence)
                    nname = str(alignment.title)
                    new_fasta_out.write(">" + nname + "\n" + sequence + "\n")
                    #input()
                    break
                break
            break





