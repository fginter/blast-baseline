#reformat tsv to fasta
for f in taxonomy_task/*.tsv
do
    python3 data2fasta.py < $f > ${f%.tsv}.fasta
done

#make local blast db from training data
makeblastdb -in taxonomy_task/taxonomy-train.fasta -dbtype prot

#blast the dev file
blastp -query taxonomy_task/taxonomy-dev.fasta -db taxonomy_task/taxonomy-train.fasta -outfmt "7 qacc sacc evalue" -max_target_seqs 10 -out dev_blasted.txt

#calculate 1-NN accuracy
python3 quick_check.py < dev_blasted.txt
