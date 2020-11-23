# GFFalign

This script was written as part of the EOSC-Life Demonstrator 4 project.

The main goal is to suggest missing or differently annotated genes in a syntenic region of a genome (query) aligned with the genome of a related species (target).
The script will check if a gene in the target genome is present in the query one. If a gene in the aligned region is present in the target genome but absent in the query one, the script suggests the new genes coordinates.
Optionally, the coordinates of genes annotated differently (longer, shorter or with a different frame) can also be showed.

The output will be a GFF file. In the last column of the output file there will be also the functional annotation of the target for the suggested gene.

As input it accept an alignment in TAB format and the two GFF files of the aligned genomes.


## Test the script

To test the script the are some small example file in the Test folder.
To use them you can try the following command:

`gffalign -m genome_aln.tab query.gff target.gff`

inside the test folder.

The outout should be something like this:

```
scaffold7	prediction	gene	967081	968380	.	963768	.	ID=scaffold7;New_annotation='ID=gene2900;Dbxref=GeneID:105913423;Name=LOC105913423;gbkey=Gene;gene=LOC105913423;gene_biotype=lncRNA';Note=new
scaffold21	prediction	gene	1066913	1069210	.	1062549	.	ID=scaffold21;New_annotation='ID=gene518;Dbxref=GeneID:105888784;Name=LOC105888784;gbkey=Gene;gene=LOC105888784;gene_biotype=protein_coding';Note=new
scaffold27	prediction	gene	2109210	2112138	.	2106448	.	ID=scaffold27;New_annotation='ID=gene19467;Dbxref=GeneID:105906405;Name=tshz2;gbkey=Gene;gene=tshz2;gene_biotype=protein_coding';Note=new
```

It's also possible to run the simple script test_gffalign.py
