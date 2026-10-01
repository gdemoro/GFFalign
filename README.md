# **This repository is no longer actively maintained**


# GFFalign

This script was written as part of the EOSC-Life Demonstrator 4 project.

The main goal is to identify missing or differently annotated genes in a syntenic region of a query genome aligned to a related target genome.
The script checks whether genes annotated in the target genome are also present in the corresponding region of the query genome. If a gene is present in the target but absent from the query annotation, GFFalign suggests its coordinates in the query genome.

Optionally, it can also report genes with discordant annotations, such as differences in length or reading frame.

The output is a GFF file. The final column also includes the functional annotation of the corresponding target gene.
As input, it accepts an alignment in TAB format together with the GFF files of the query and target genomes.

## Test the script

To test the script, some small example files are available in the `Test` folder.
Run the following command from inside the test folder:

`gffalign -m genome_aln.tab query.gff target.gff`


The output should look similar to this:
```
scaffold7	prediction	gene	967081	968380	.	963768	.	ID=scaffold7;New_annotation='ID=gene2900;Dbxref=GeneID:105913423;Name=LOC105913423;gbkey=Gene;gene=LOC105913423;gene_biotype=lncRNA';Note=new
scaffold21	prediction	gene	1066913	1069210	.	1062549	.	ID=scaffold21;New_annotation='ID=gene518;Dbxref=GeneID:105888784;Name=LOC105888784;gbkey=Gene;gene=LOC105888784;gene_biotype=protein_coding';Note=new
scaffold27	prediction	gene	2109210	2112138	.	2106448	.	ID=scaffold27;New_annotation='ID=gene19467;Dbxref=GeneID:105906405;Name=tshz2;gbkey=Gene;gene=tshz2;gene_biotype=protein_coding';Note=new
```

It is also possible to run the simple `test_gffalign.py` script.
