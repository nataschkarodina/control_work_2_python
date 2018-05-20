## control_work_2_python
## created by Natalia Rodina

### This skript takes as input a fasta files with not named contigs, blasts it using blast n and creates as output a new fasta file, where the contigs are named after the organism that match most. 

### Make sure, your inout file is in the same directory as the skript. Or write a path in the following line:

```
records = SeqIO.parse("classwork2.fasta", format="fasta")
```

### Your otput file will be named new_fasta.fasta and will be in fasta format
